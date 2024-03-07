from django.db import models
from django.utils import timezone


# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phoneno = models.IntegerField()
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at=models.DateTimeField(default=timezone.now)

class photos(models.Model):
    bridePhoto=models.ImageField(upload_to='images/bride'),
    protraitPhoto=models.ImageField(upload_to='images/protrait')