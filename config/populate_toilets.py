import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility

# Sample toilet data
toilets_data = [
    {
        'name': 'Men\'s Restroom - Block A Ground Floor',
        'location_type': 'TOILET',
        'block': 'A',
        'floor': 0,
        'gender': 'MALE',
    },
    {
        'name': 'Women\'s Restroom - Block A Ground Floor',
        'location_type': 'TOILET',
        'block': 'A',
        'floor': 0,
        'gender': 'FEMALE',
    },
    {
        'name': 'Men\'s Restroom - Block A First Floor',
        'location_type': 'TOILET',
        'block': 'A',
        'floor': 1,
        'gender': 'MALE',
    },
    {
        'name': 'Women\'s Restroom - Block A First Floor',
        'location_type': 'TOILET',
        'block': 'A',
        'floor': 1,
        'gender': 'FEMALE',
    },
    {
        'name': 'Men\'s Restroom - Block B Ground Floor',
        'location_type': 'TOILET',
        'block': 'B',
        'floor': 0,
        'gender': 'MALE',
    },
    {
        'name': 'Women\'s Restroom - Block B Ground Floor',
        'location_type': 'TOILET',
        'block': 'B',
        'floor': 0,
        'gender': 'FEMALE',
    },
    {
        'name': 'Men\'s Restroom - Block B First Floor',
        'location_type': 'TOILET',
        'block': 'B',
        'floor': 1,
        'gender': 'MALE',
    },
    {
        'name': 'Women\'s Restroom - Block B First Floor',
        'location_type': 'TOILET',
        'block': 'B',
        'floor': 1,
        'gender': 'FEMALE',
    },
    {
        'name': 'Men\'s Restroom - Block C Ground Floor',
        'location_type': 'TOILET',
        'block': 'C',
        'floor': 0,
        'gender': 'MALE',
    },
    {
        'name': 'Women\'s Restroom - Block C Ground Floor',
        'location_type': 'TOILET',
        'block': 'C',
        'floor': 0,
        'gender': 'FEMALE',
    },
]

print('Creating toilet records...')
for data in toilets_data:
    toilet, created = Facility.objects.get_or_create(
        name=data['name'],
        defaults=data
    )
    if created:
        print(f'✓ Created: {toilet.name}')
    else:
        print(f'- Already exists: {toilet.name}')

print(f'\n✅ Done! Total toilets in database: {Facility.objects.filter(location_type="TOILET").count()}')
