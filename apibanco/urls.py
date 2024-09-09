"""
URL configuration for apibanco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from bd import views

from bd .views import UsuarioListCreate

urlpatterns = [
    path('usuario/', views.UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuario/<str:cpf>/', views.UsuarioDetail.as_view(), name='usuario-detail'),
    path('ec2/', views.list_ec2_instances, name='list_ec2_instances'),
]
