from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventBooking
from django.contrib.auth.decorators import login_required

# List of available events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_booking/event_list.html', {'events': events})

# Event details view
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_booking/event_detail.html', {'event': event})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(EventBooking, id=booking_id)
    return render(request, 'event_booking/booking_confirmation.html', {'booking': booking})

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        number_of_tickets = int(request.POST['number_of_tickets'])
        total_price = event.ticket_price * number_of_tickets

        # Check if there are enough tickets available
        if event.tickets_sold + number_of_tickets <= event.total_tickets:
            # Create the EventBooking record
            booking = EventBooking.objects.create(
                event=event,
                user=request.user,
                number_of_tickets=number_of_tickets,
                total_price=total_price
            )
            # Update the tickets_sold count
            event.tickets_sold += number_of_tickets
            event.save()

            return redirect('event_booking:booking_confirmation', booking_id=booking.id)
        else:
            # If not enough tickets are available, render an error page or message
            return render(request, 'event_booking/event_unavailable.html', {'event': event})

    return render(request, 'event_booking/book_event.html', {'event': event})

