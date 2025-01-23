from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import Account
from expenses.models import AcccountEntry

@login_required
def index(request):
    accountentries = AcccountEntry.objects.all()
    return render(request, 'expenses/index.html',{"accountentries": accountentries})



def addexpense(request):
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


def delete_expense(request, account_id):
    account = Account.objects.get(id= expense.debit_account_id)
    account.delete()
    accounts = Account.objects.all()
    return render(request, 'partials/accounts.html', {'accountentries': accountentries})