from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import Account

@login_required
def home(request):
    accounts = Account.objects.all()
    return render(request, 'home.html', {'accounts': accounts})


