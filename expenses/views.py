from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from expenses.models import AcccountEntry

@login_required
def index(request):
    return render(request, 'expenses/index.html')


def addexpense(request):
    data = request.POST
    expense = AcccountEntry()
    expense.amount = data['amount']
    expense.currency = data['currency']
    expense.date = data['date']
    expense.comment = data['comment']
    expense.save()
    return redirect('index')


