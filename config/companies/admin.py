from django.contrib import admin
from .models import Company

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
