from django.db import models

# Create your models here.
# ORM - Object Relational Mapping
# SQL - Structured Query Language
    

class Category(models.Model):
     id = models.AutoField(primary_key=True)
     image_file =  models.ImageField(upload_to='images/', null=True, blank=True)
     name = models.CharField(max_length=120)
     is_expense = models.BooleanField()



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

