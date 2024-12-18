from django.shortcuts import render, get_object_or_404, redirect
from .models import Cab, CabBooking
from django.contrib.auth.decorators import login_required
from datetime import datetime
from decimal import Decimal  # Import Decimal to handle conversions

# List of available cabs
def cab_list(request):
    cabs = Cab.objects.all()
    return render(request, 'cab_booking/cab_list.html', {'cabs': cabs})

def estimate_fare(request, cab_id):
    cab = get_object_or_404(Cab, id=cab_id)
    estimated_fare = None
    distance = pickup_location = drop_location = pickup_time = None
    
    if request.method == 'POST':
        # Use get() to handle missing fields gracefully
        distance = request.POST.get('distance')
        pickup_location = request.POST.get('pickup_location')
        drop_location = request.POST.get('drop_location')
        pickup_time = request.POST.get('pickup_time')
        
        # Ensure all required fields are present
        if distance:
            distance = Decimal(distance)
            estimated_fare = cab.base_fare + (distance * cab.per_km_rate)

    return render(request, 'cab_booking/fare_estimation.html', {
        'cab': cab,
        'estimated_fare': estimated_fare,
        'distance': distance,
        'pickup_location': pickup_location,
        'drop_location': drop_location,
        'pickup_time': pickup_time,
    })

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(CabBooking, id=booking_id)
    return render(request, 'cab_booking/booking_confirmation.html', {'booking': booking})

@login_required
def book_cab(request, cab_id):
    cab = get_object_or_404(Cab, id=cab_id)
    if request.method == 'POST':
        pickup_location = request.POST['pickup_location']
        drop_location = request.POST['drop_location']
        pickup_time = request.POST['pickup_time']  # Already in the correct format from the form
        distance = Decimal(request.POST['distance'])
        estimated_fare = cab.base_fare + (distance * cab.per_km_rate)

        # Create the CabBooking record
        booking = CabBooking.objects.create(
            cab=cab,
            user=request.user,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_time=pickup_time,
            distance=distance,
            estimated_fare=estimated_fare
        )
        return redirect('cab_booking:booking_confirmation', booking_id=booking.id)

    return render(request, 'cab_booking/book_cab.html', {'cab': cab})


