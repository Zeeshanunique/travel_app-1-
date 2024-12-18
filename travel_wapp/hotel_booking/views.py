from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Booking
from django.contrib.auth.decorators import login_required
from datetime import datetime

# List of hotels
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_booking/hotel_list.html', {'hotels': hotels})

# Hotel details view
def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotel_booking/hotel_detail.html', {'hotel': hotel})

def booking_confirmation(request, booking_id):
    # Retrieve the booking by ID or return 404 if not found
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Render the confirmation template and pass booking details
    return render(request, 'hotel_booking/booking_confirmation.html', {'booking': booking})

# def booking_confirmation(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     return render(request, 'hotel_booking/booking_confirmation.html', {'booking': booking})

@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        check_in_date = datetime.strptime(request.POST['check_in_date'], "%Y-%m-%d")
        check_out_date = datetime.strptime(request.POST['check_out_date'], "%Y-%m-%d")
        guests = int(request.POST['guests'])
        total_days = (check_out_date - check_in_date).days
        total_price = hotel.price_per_night * total_days * guests

        # Ensure 'total_price' is included if it exists in the model
        booking = Booking.objects.create(
            hotel=hotel,
            user=request.user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guests=guests,
            total_price=total_price
        )
        return redirect('hotel_booking:booking_confirmation', booking_id=booking.id)
    
    return render(request, 'hotel_booking/book_hotel.html', {'hotel': hotel})

# Book a hotel
@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        guests = int(request.POST['guests'])
        total_days = (datetime.strptime(check_out_date, "%Y-%m-%d") - datetime.strptime(check_in_date, "%Y-%m-%d")).days
        total_price = hotel.price_per_night * total_days * guests

        booking = Booking.objects.create(
            hotel=hotel,
            user=request.user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guests=guests,
            total_price=total_price
        )
        return redirect('hotel_booking:booking_confirmation', booking_id=booking.id)
    
    return render(request, 'hotel_booking/book_hotel.html', {'hotel': hotel})
