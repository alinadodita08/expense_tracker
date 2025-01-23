
from django.urls import path 
from . import views

urlpatterns = [
    path('create/', views.create_account, name='create_account'),
    path('delete/<int:account_id>/', views.delete_account, name='delete_account'),
    path('details/<int:account_id>/', views.details, name='details_account'),
    path('edit/', views.edit_account, name='edit_account'),
]
