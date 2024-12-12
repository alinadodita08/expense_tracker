from django.shortcuts import redirect, render
from .models import Account
# Create your views here.


def create_account(request):
    data = request.POST
    account = Account()
    account.name = data['name']
    account.balance = data['balance']
    account.currency = data['currency']
    account.save()
    return redirect('home')


def delete_account(request):
    pass


def update_account(request):
    pass