from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('make/', views.make_appointment, name='make_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
]