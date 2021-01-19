# Airline
Airline Django Project

# Startup
- pip install django
- django-admin startproject projectname
- python manage.py startapp appname
- python manage.py makemigrations
- python manage.py migrate


--------------------------------------
# Project Structure
- create new python file -> urls.py under the appname
-------------------------------------
-  ' __str__() '  funcion returns the "string" representation of the object

-------------------------------------
# Database Operations
- >>> from flights.models import Airport, Flight
- >>> one = Airport(code="First", city="New York")
- >>> two = Airport(code = "Second", city = "London")
- >>> one.save()
- >>> two.save()
- >>> f = Flight(origin=one, destination=two, duration=125)
- >>> f.save()
- >>> f.origin
=> <Airport: New York (First)>
- >>> f.destination
=> <Airport: London (Second)>
- >>> f
=> <Flight: 1 - New York (First) to London (Second)>
- >>> f.origin.code
=> 'First'


# Register model to admin (Admin Site)
- admin.py => admin.site.register(modelname)
- cmd => python manage.py createsuperuser


- cmd=> python manage.py shell
- from flights.models import Flight, Passenger
- f = Flight.objects.get(pk=1)
- f
- p = Passenger(first="Alice", last="Genny")
- p.save()
- p.flight
- p.flight.add(f)
- p.flight.all() 

- f.passengers.all()
-----------------------------------------------------------------------
# Django authentication
- django.contrib.auth
-----------------------------------------------------------------------
# Templates Tags in Django
- in operator => The in operator will check whether the number is in the list or not.
{% if number in list %}
    <p>Yes the number is in the list</p>
{% endif %}
