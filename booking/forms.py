from django import forms
from .models import Appointment, Branch
from django.utils import timezone
from datetime import datetime, timedelta

class HourChoiceField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        choices = [(str(hour), f"{hour:02}:00") for hour in range(24)]
        super().__init__(choices=choices, *args, **kwargs)

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.SelectDateWidget(), label="Appointment Date")
    appointment_hour = HourChoiceField(label="Appointment Hour")

    class Meta:
        model = Appointment
        fields = ['branch']

    def save(self, commit=True):
        instance = super().save(commit=False)
        date = self.cleaned_data['appointment_date']
        hour = int(self.cleaned_data['appointment_hour'])
        chosen_datetime = datetime.combine(date, datetime.min.time()) + timedelta(hours=hour)
        instance.appointment_time = chosen_datetime
        if commit:
            instance.save()
        return instance