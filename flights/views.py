from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Flight
def index(request):
    contex = {
        "flights": Flight.objects.all()
    }
    print(contex)
    return render(request, 'flights/index.html', contex)