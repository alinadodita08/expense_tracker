from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import Account
from expenses.models import AcccountEntry

@login_required
def index(request):
    return render(request, 'expenses/index.html')


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


