import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility

print(f'Total Facilities: {Facility.objects.count()}')
print(f'Toilets: {Facility.objects.filter(location_type="TOILET").count()}')
print('\nToilet records:')
toilets = Facility.objects.filter(location_type='TOILET')
for t in toilets:
    print(f'  - {t.name} | Gender: {t.gender} | Block: {t.block} | Floor: {t.floor}')
