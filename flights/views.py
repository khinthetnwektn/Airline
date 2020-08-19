from django.shortcuts import render

from django.http import HttpResponse, Http404
# Create your views here.
from .models import Flight
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
        "flight": flight
    }

    return render(request, 'flights/flight.html', context)