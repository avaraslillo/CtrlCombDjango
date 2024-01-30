from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if is_ajax(request=self.request):
            return JsonResponse(form.errors,status=400)
        else:
            return response
        
class SinAutorizacion(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      MixinFormInvalid):

    login_url = "bases:login"
    raise_exception = False
    redirect_field_name = "redirect_to"
    def handle_no_permission(self):
        from django.http import HttpResponsePermanentRedirect
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = "pages:forbidden"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


def primera_vista(request):
    return HttpResponse("Hola Mundo, desde el <b>Curso de Django para profesiones de Daniel Bojorge</b>")

class HomeView(TemplateView):
    template_name = "bases/home.html"

class MixinSaveUser:
    def form_valid(self, form):
        print(f"**************{form.instance.id} --- {self.request.user.id} ***************") 

        if form.instance.id:
            form.instance.um = self.request.user
        else:
            form.instance.uc = self.request.user

        return super().form_valid(form) 