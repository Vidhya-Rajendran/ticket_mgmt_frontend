"""ticket_mgmt_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

app_name = 'ticket'

urlpatterns = [
    path('tickets/', views.ticket_list, name='list'),
    path('ticket/create/', views.create_ticket, name='create'),
    path('ticket/<int:id>/', views.view_ticket, name='view'),
    path('ticket/<int:id>/edit/', views.edit_ticket, name='edit'),
    path('ticket/<int:id>/delete/', views.delete_ticket, name='delete'),
]