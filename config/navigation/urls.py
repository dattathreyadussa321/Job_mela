from django.urls import path
from .views import scan_location

urlpatterns = [
    path('scan/<int:location_id>/', scan_location, name='scan_location'),
]
