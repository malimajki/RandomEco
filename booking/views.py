from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Appointment, Branch
from .forms import AppointmentForm

@login_required
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            
            # Check if user has another appointment within 14 days
            fourteen_days_ago = timezone.now() - timedelta(days=14)
            recent_appointments = Appointment.objects.filter(
                user=request.user,
                appointment_time__gte=fourteen_days_ago
            )
            if recent_appointments.exists():
                form.add_error(None, 'You can only make an appointment once every 14 days.')
            else:
                # Check if the branch is fully booked at this time
                branch_appointments = Appointment.objects.filter(
                    branch=appointment.branch,
                    appointment_time=appointment.appointment_time
                )
                if branch_appointments.count() >= 3:
                    form.add_error(None, 'This branch is fully booked at the chosen time.')
                else:
                    appointment.save()
                    return redirect('appointments:appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/make_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')
