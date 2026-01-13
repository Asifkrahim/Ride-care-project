from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Maintenance

@login_required
def dashboard(request):
    if request.method=='POST':
        vehicle=request.POST['vehicle']
        maintenance_type=request.POST['maintenance']
        odometer=int(request.POST['odometer'])
        date=request.POST['date']

        if vehicle=='bike':
            intervals={'oil':3000, 'brake':10000, 'air_filter':6000}
        else:
            intervals={'oil':5000, 'brake':20000, 'air_filter':10000}

        try:
            next_service=odometer+intervals[maintenance_type]

            Maintenance.objects.create(
                user=request.user,
                vehicle_type=vehicle,
                maintenance_type=maintenance_type,
                odometer=odometer,
                date=date,
                next_service_odometer=next_service
            )
            messages.success(request, "Maintenance record added successfully!")
        except Exception as e:
            messages.error(request, f"Error adding record: {e}")

    records=Maintenance.objects.filter(user=request.user)
    return render(request, 'dashboard.html',{'records':records})


