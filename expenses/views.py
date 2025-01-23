from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import Account
from expenses.models import AcccountEntry

@login_required
def index(request):
    accountentries = AcccountEntry.objects.all()
    return render(request, 'expenses/index.html', {'accountentries': accountentries})


def add_expense(request):
    data = request.POST
    account = Account.objects.first()
    expense = AcccountEntry()
    expense.debit_account_id = account
    expense.amount = data['amount']
    expense.currency = data['currency']
    expense.date = data['date']
    expense.comment = data['comment']
    expense.save()
    return redirect('expenses')


def delete_expense(request, id):
    expense = AcccountEntry.objects.get(id=id)
    expense.delete()
    accountentries = AcccountEntry.objects.all()
    return render(request, 'expenses/delete.html', {'accountentries': accountentries})

