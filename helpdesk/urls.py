"""
URL configuration for djangoUniProjectFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from helpdesk.views import create_ticket, tickets_list, ticket_detail


urlpatterns = [
    path('', views.home, name=''),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")), name='favicon'),
    path('create_ticket/', create_ticket, name='create_ticket'),
    path('update_ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('tickets/', tickets_list, name='tickets_list'),
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
