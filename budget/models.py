from django.db import models

# Create your models here.
# ORM - Object Relational Mapping
# SQL - Structured Query Language


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name
    

class Category(models.Model):
     id = models.AutoField(primary_key=True)
     image_file =  models.ImageField(upload_to='images/', null=True, blank=True)
     name = models.CharField(max_length=120)
     is_expense = models.BooleanField()


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


class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10,decimal_places=2 )
    month = models.IntegerField()


class BudgetBracket(models.Model):
        id = models.AutoField(primary_key=True)
        budget_id = models.ForeignKey(Budget,on_delete=models.CASCADE, related_name='budget')
        name = models.CharField(max_length=120)
        total = models.DecimalField(max_digits=10,decimal_places=2 )


class Category2BudgetBracket(models.Model):
     id = models.AutoField(primary_key=True)
     category_id = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='budget_bracket_category' )
     budget_bracket_id = models.ForeignKey(BudgetBracket,on_delete=models.CASCADE, related_name='budget_bracket')

