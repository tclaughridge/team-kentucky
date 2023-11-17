from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.getProviders, name='index'),
    path('filter/', views.filterProviders, name='filter'),
    path("admin/", admin.site.urls)
]
