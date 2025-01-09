from django.shortcuts import redirect, render
from .models import Account
# Create your views here.

# CRUD - Create, Read, Update, Delete

def create_account(request):
    data = request.POST
    account = Account()
    account.name = data['name']
    account.balance = data['balance']
    account.currency = data['currency']
    account.save()
    return redirect('home')


def delete_account(request, account_id):
    account = Account.objects.get(id=account_id)
    account.delete()
    accounts = Account.objects.all()
    return render(request, 'partials/accounts.html', {'accounts': accounts})


def edit_account_data(request, account_id):
    account = Account.objects.get(id=account_id)
    return render(request, 'partials/edit.html', {'account': account})


def edit_account(request):
    data = request.POST
    account = Account.objects.get(id=data['id'])
    account.name = data['name']
    account.balance = data['balance']
    account.currency = data['currency']
    account.save()
    return redirect('home')