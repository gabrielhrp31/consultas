"""odonto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # patients urls
    path('list', views.list_patients, name="list_patients"),
    path('get', views.get_patients, name="get_patients"),
    path('new/', views.new_patient, name="new_patient"),
    path('edit/<int:id>/', views.edit_patient, name="edit_patient"),
    path('view/<int:id>/', views.view_patient, name="view_patient"),
    path('get/<int:id>/', views.get_patient, name="get_patient"),
    path('delete/<int:id>/', views.delete_patient, name="delete_patient"),
    # addresses urls
    path('address/list/', views.list_address, name="list_address"),
    path('address/get/', views.get_address, name="get_address"),
    path('address/new/', views.new_address, name="new_address"),
    path('address/view_edit/<int:id>/', views.view_edit_address, name="view_edit_address"),
    path('address/delete/<int:id>/', views.delete_address, name="delete_address"),
]
