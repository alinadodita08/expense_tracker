"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path 
from budget import views
from account import views as account_views
from expenses import views as expenses_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('create_account/', account_views.create_account, name='create_account'),
    path('delete_account/<int:account_id>/', account_views.delete_account, name='delete_account'),
    path('edit_account_data/<int:account_id>/', account_views.edit_account_data, name='edit_account_data'),
    path('edit_account/', account_views.edit_account, name='edit_account'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('expenses/', expenses_views.index, name='expenses')
]
