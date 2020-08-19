from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Flight, Passenger


def index(request):
    contex = {
        "flights": Flight.objects.all()
    }
    print(contex)
    return render(request, 'flights/index.html', contex)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exit.")
    context = {
        "flight": flight,
        "passengers": Passenger.objects.all(),
        "non-passengers": Passenger.objects.exclude(flights=flight).all() #select filter
    }
    return render(request, 'flights/flight.html', context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)

    except KeyError:
        return render(request, 'flights/error.html', {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, 'flights/error.html', {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, 'flights/error.html', {"message": "No passenger."})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))