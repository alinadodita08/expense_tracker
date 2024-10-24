from django.db import models

# Create your models here.
# ORM - Object Relational Mapping
# SQL - Structured Query Language


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name
