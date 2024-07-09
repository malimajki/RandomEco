from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

class Appointment(models.Model):
    user = models.ForeignKey(User, related_name="appointments", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, related_name="appointments", on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)