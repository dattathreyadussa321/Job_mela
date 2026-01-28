from navigation.models import Location
from django.shortcuts import redirect, render
from companies.models import Company
from django.shortcuts import get_object_or_404
from navigation.models import Location, Route
from collections import defaultdict



def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)

    current_location_id = request.session.get("current_location")
    current_location = None
    directions = None

    if current_location_id:
        current_location = Location.objects.filter(id=current_location_id).first()

    if current_location and company.venue:
        directions = f"""
        Start from {current_location.name}
        → Block {company.block}
        → Floor {company.floor}
        → Room {company.room_number}
        """

    return render(
        request,
        "dashboard/company_detail.html",
        {
            "company": company,
            "directions": directions,
            "current_location": current_location,
        }
    )

def set_current_location(request):
    if request.method == 'POST':
        request.session['current_location_id'] = request.POST.get('location_id')
    return redirect('home')

def home(request):
    locations = Location.objects.all()
    companies = Company.objects.all()

    current_location = None
    loc_id = request.session.get('current_location_id')
    if loc_id:
        current_location = Location.objects.get(id=loc_id)

    return render(request, 'dashboard/home.html', {
        'companies': companies,
        'locations': locations,
        'current_location': current_location,
    })


def facilities(request):
    """
    Show facilities like CANTEEN, LIBRARY
    Filtered by ?type=CANTEEN
    """
    facility_type = request.GET.get("type")

    facilities = Facility.objects.all()
    if facility_type:
        facilities = facilities.filter(location_type=facility_type)

    context = {
        "facilities": facilities
    }
    return render(request, "dashboard/facilities.html", context)

def toilets(request):
    """
    Display toilets, optionally filtered by gender
    ?gender=MALE / FEMALE
    """
    gender = request.GET.get("gender")

    toilets = Facility.objects.filter(location_type="TOILET")

    if gender:
        toilets = toilets.filter(gender=gender)

    context = {
        "toilets": toilets
    }
    return render(request, "dashboard/toilets.html", context)    
