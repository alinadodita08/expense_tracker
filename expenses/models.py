from django.db import models

from account.models import Account
from budget.models import Category

class AcccountEntry(models.Model):
    id = models.AutoField(primary_key=True)
    debit_account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_account', null=True, blank=True)
    credit_account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_account', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    currency = models.CharField(max_length=3, default='USD')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='account_name_category', null=True, blank=True)


def __str__(self):
    return self.id