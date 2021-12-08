"""django_crud_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apps.person.views import homepage, add_person, edit_person, delete_person
from apps.person.class_based_views import PersonList, PersonCreate, PersonUpdate, PersonDelete

urlpatterns = [
    path('admin/', admin.site.urls),

    #""""Function based views urls"""

    #path('', homepage, name='homepage'),
    #path('add/', add_person, name='add'),
    #path('edit/<int:id>/', edit_person, name='edit'),
    #path('delete/<int:id>/', delete_person, name='delete'),

    #"""Class based views urls"""
    path('', PersonList.as_view(), name = 'homepage'),
    path('add/', PersonCreate.as_view(), name = 'add'),
    path('edit/<int:pk>', PersonUpdate.as_view(), name = 'edit'),
    path('delete/<int:pk>', PersonDelete.as_view(), name = 'delete'),
]
