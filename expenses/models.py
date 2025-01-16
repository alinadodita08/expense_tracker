from django.db import models

from account.models import Account
from budget.models import Category

class AcccountEntry(models.Model):
    id = models.AutoField(primary_key=True)
    debit_account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_account')
    credit_account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_account')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='account_name_category')


def __str__(self):
    return self.id