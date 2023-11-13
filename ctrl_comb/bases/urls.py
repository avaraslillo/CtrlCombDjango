from django.urls import path,include

from .views import *


app_name="core"


urlpatterns = [
    #path('',primera_vista,name="primera_vista")
    path('',HomeView.as_view(),name="home")
]
