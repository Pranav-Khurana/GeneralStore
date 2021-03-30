from django.views.generic import TemplateView
from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    #path('',TemplateView.as_view(template_name='contact.html'), name='home'),
    #path('list/', views.list, name='index'),
    #path('', views.list.as_view(), name='index')
] 
