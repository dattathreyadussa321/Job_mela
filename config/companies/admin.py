from django.contrib import admin
from .models import Company, Facility

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number', 'venue')
    search_fields = ('name',)
    list_filter = ('venue',)

    fields = (
        'name',
        'profile_url',
        'jd',
        'jd_file',
        'room_number',
        'venue',
        'block',
        'floor',
        'landmark',
    )

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type', 'gender', 'block', 'floor', 'room_number')
    search_fields = ('name', 'block')
    list_filter = ('location_type', 'gender', 'block')
    
    fields = (
        'name',
        'location_type',
        'gender',
        'block',
        'floor',
        'room_number',
    )
