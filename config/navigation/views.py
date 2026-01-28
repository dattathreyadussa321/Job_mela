from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import Location

def scan_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    # Save current location in session
    request.session['current_location'] = location.name

    return redirect('home')
