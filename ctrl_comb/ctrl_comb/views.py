from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *

from .forms import *

# Create your views here.


class MarkList(LoginRequiredMixin,ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name = "obj"
    ordering=["id"]
    login_url="usuarios:login"


def mark_save(request):
    context = {}
    template_name = "ctrl_comb/mark-list.html"

    if request.method == "POST":
        i = request.POST.get("id")
        d = request.POST.get("descript")

        o = None
        
        if i:
            o = Mark.objects.filter(id=i).first()
        else:
            o = Mark.objects.filter(descript = d).first()

        if o:
            o.descript = d
            o.save()
        else:
            o = Mark.objects.create(descript = d)    
    
    obj = Mark.objects.all().order_by("id")
    r = Mark.objects.filter(id = o.id).first()
    context["obj"] = obj
    context["reg"] = r

    return render(request,template_name,context)

def mark_delete(request,pk):
    context={}
    template_name="ctrl_comb/mark-list.html"

    o = Mark.objects.filter(id=pk).first()
    o.delete()

    obj = Mark.objects.all().order_by("id")
    context["obj"] = obj

    return render(request,template_name,context)

def mark_edit(request,pk=None):

    context={}
    template_name="ctrl_comb/mark-frm.html"

    if pk:
        o = Mark.objects.filter(id=pk).first()
        frm = MarkForm(instance=o)
    else:
        frm=MarkForm()

    context["form"] = frm
    context["obj"] = o

    return render(request,template_name,context)

class ModeloList(LoginRequiredMixin, ListView):
    template_name="ctrl_comb/modelo.html"
    model=Modelo
    context_object_name = "obj"
    ordering=["mark","descript"]
    login_url = "usuarios:login"



class ModeloNew(CreateView):
    model=Modelo
    template_name="ctrl_comb/modelo_form.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")

class ModeloEdit(UpdateView):
    model=Modelo
    template_name="ctrl_comb/modelo_form.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list") 

class ModeloDelete(DeleteView):
    model=Modelo
    template_name="bases/delete.html"
    context_object_name="obj"
    success_url=reverse_lazy("control:modelo_list") 

class ModeloEditModal(UpdateView):
    model=Modelo
    template_name="ctrl_comb/modelo_modal.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list") 

class ModeloNewModal(CreateView):
    model=Modelo
    template_name="ctrl_comb/modelo_modal.html"
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")

@login_required(login_url="usuarios:login")
def modelo_dt(request):
    context = {}
    datos = request.GET
    draw = int(datos.get("draw"))
    start = int(datos.get("start"))
    length = int(datos.get("length"))
    search = datos.get("search[value]")

    registros = Modelo.objects.all()

    if search:
        registros = registros.filter(
            Q(mark__descript__icontains=search) | 
            Q(descript__icontains=search)

        )

    recordsTotal = registros.count()
   # recordsFiltered = recordsTotal

    context["draw"] = draw
    context["recordsTotal"] = recordsTotal
    context["recordsFiltered"] = recordsTotal

    reg = registros[start:start + length]

    paginator = Paginator(reg,length)

    try:
        obj = paginator.page(draw).object_list
    except PageNotAnInteger:
        obj = paginator.page(draw).object_list
    except EmptyPage:
        obj = paginator.page(paginator.num_pages).object_list
    #datos = []
    #for o in obj:
     #   datos.append({"id":o.id,"mark":o.mark__descript,"descript":o.descript})

    datos = [
        {
            "id" : o.id, "mark" : o.mark.descript,"descript" : o.descript

        } for o in obj

    ]

    context["datos"]=datos
    return JsonResponse(context,safe=False)














