from django.shortcuts import render
from django.views.generic import *

from .models import *

from .forms import *

# Create your views here.


class MarkList(ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name = "obj"
    ordering=["id"]


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






