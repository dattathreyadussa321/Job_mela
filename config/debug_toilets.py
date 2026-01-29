import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility

print("=" * 70)
print("COMPREHENSIVE FACILITY DATABASE DEBUG")
print("=" * 70)

# Get ALL facilities
all_facilities = Facility.objects.all()
print(f'\n📊 Total Facilities in Database: {all_facilities.count()}')

# Show ALL facilities with their types
print("\n" + "=" * 70)
print("ALL FACILITIES IN DATABASE:")
print("=" * 70)
for f in all_facilities:
    print(f'\nID: {f.id}')
    print(f'  Name: {f.name}')
    print(f'  Type: "{f.location_type}" (choices: {dict(Facility.LOCATION_TYPES).get(f.location_type, "INVALID")})')
    print(f'  Gender: "{f.gender}" ({f.get_gender_display() if f.gender else "None"})')
    print(f'  Block: {f.block}, Floor: {f.floor}')

# Check the exact filter used in views
print("\n" + "=" * 70)
print("TESTING VIEW FILTER: location_type='TOILET'")
print("=" * 70)
toilets_filtered = Facility.objects.filter(location_type='TOILET')
print(f'Found: {toilets_filtered.count()} toilets')

# Check for case sensitivity or whitespace issues
print("\n" + "=" * 70)
print("CHECKING FOR COMMON ISSUES:")
print("=" * 70)
for f in all_facilities:
    if f.location_type != 'TOILET':
        print(f'❌ {f.name}')
        print(f'   location_type = "{f.location_type}" (length: {len(f.location_type)})')
        print(f'   Expected: "TOILET"')
        # Check if it's a case or whitespace issue
        if f.location_type.strip().upper() == 'TOILET':
            print(f'   ⚠️  Has whitespace or case issue!')
    else:
        print(f'✅ {f.name} - Correct location_type')

print("\n" + "=" * 70)
print("LOCATION_TYPE FIELD ANALYSIS:")
print("=" * 70)
location_types = all_facilities.values_list('location_type', flat=True).distinct()
print(f'Distinct location_type values in DB: {list(location_types)}')
print(f'Valid choices: {[choice[0] for choice in Facility.LOCATION_TYPES]}')
