from django.contrib import admin
from .models import Location, Route

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')
    list_filter = ('location_type',)
    search_fields = ('name',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('from_location', 'to_location')
    search_fields = ('from_location__name', 'to_location__name')
