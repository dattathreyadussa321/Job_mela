import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility
from django.db import connection

print("=" * 70)
print("DATABASE CONNECTION TEST")
print("=" * 70)

# Show database file location
from django.conf import settings
print(f"\nDatabase: {settings.DATABASES['default']['NAME']}")

# Show raw SQL query result
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM companies_facility")
    count = cursor.fetchone()[0]
    print(f"\nRaw SQL Count: {count}")
    
    cursor.execute("""
        SELECT id, name, location_type, gender, block, floor 
        FROM companies_facility 
        ORDER BY id DESC 
        LIMIT 20
    """)
    rows = cursor.fetchall()
    
    print("\n" + "=" * 70)
    print("RAW DATABASE RECORDS (Last 20):")
    print("=" * 70)
    
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"  Name: {row[1]}")
        print(f"  Type: {row[2]}")
        print(f"  Gender: {row[3]}")
        print(f"  Block: {row[4]}, Floor: {row[5]}")

# Now check via ORM
print("\n" + "=" * 70)
print("ORM QUERY RESULT:")
print("=" * 70)
print(f"Facility.objects.count(): {Facility.objects.count()}")
print(f"Facility.objects.filter(location_type='TOILET').count(): {Facility.objects.filter(location_type='TOILET').count()}")

# Check if there are any facilities that you might have added
all_facilities = Facility.objects.all().order_by('-id')
print(f"\n" + "=" * 70)
print(f"ALL FACILITIES (via ORM): {all_facilities.count()}")
print("=" * 70)

for f in all_facilities:
    print(f"\nID: {f.id} | {f.name}")
    print(f"  Type: '{f.location_type}' | Gender: '{f.gender}' | Block: {f.block}, Floor: {f.floor}")
