from django.db import models
from django.contrib.auth.models import User
from datetime import time

class Branch(models.Model):
    name = models.CharField(max_length=100)
    opening_time = models.TimeField(default=time(9, 0))  # 9:00 AM
    closing_time = models.TimeField(default=time(17, 0))  # 5:00 PM

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()

    class Meta:
        unique_together = ('branch', 'appointment_time')

    def __str__(self):
        return f"{self.user} - {self.branch} at {self.appointment_time}"
