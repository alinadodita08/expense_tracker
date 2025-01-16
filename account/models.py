from django.db import models
from budget.models import Category
# Create your models here.

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name
    
