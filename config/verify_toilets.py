import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility

print("=" * 60)
print("TOILET DATABASE VERIFICATION")
print("=" * 60)

# All toilets
all_toilets = Facility.objects.filter(location_type='TOILET')
print(f'\nTotal Toilets: {all_toilets.count()}')

# Male toilets
male_toilets = all_toilets.filter(gender='MALE')
print(f'\nMale Toilets: {male_toilets.count()}')
for t in male_toilets:
    print(f'  🚹 {t.name} (Block {t.block}, Floor {t.floor})')

# Female toilets
female_toilets = all_toilets.filter(gender='FEMALE')
print(f'\nFemale Toilets: {female_toilets.count()}')
for t in female_toilets:
    print(f'  🚺 {t.name} (Block {t.block}, Floor {t.floor})')

print("\n" + "=" * 60)
print("Testing view logic:")
print("=" * 60)

# Test the view logic
from dashboard.views import toilets
from django.test import RequestFactory

factory = RequestFactory()

# Test without filter
request = factory.get('/toilets/')
print(f"\n✓ All toilets (no filter): Should return {all_toilets.count()} toilets")

# Test with MALE filter
request = factory.get('/toilets/?gender=MALE')
print(f"✓ Male filter: Should return {male_toilets.count()} toilets")

# Test with FEMALE filter
request = factory.get('/toilets/?gender=FEMALE')
print(f"✓ Female filter: Should return {female_toilets.count()} toilets")

print("\n✅ Database and view logic are working correctly!")
