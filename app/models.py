from django.db import models

# Create your models here.

class form(models.Model):
    name = models.CharField( max_length=50),
    email=models.EmailField( max_length=254),
    
    appointment_date=models.DateField(auto_now=False, auto_now_add=False),
