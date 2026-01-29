import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Facility

print("=" * 70)
print("REAL-TIME FACILITY MONITOR")
print("=" * 70)
print("\nThis script will check the database every 3 seconds.")
print("Add a toilet via admin panel and watch it appear here!\n")
print("Press Ctrl+C to stop.\n")

previous_count = Facility.objects.count()
print(f"Starting count: {previous_count} facilities\n")

try:
    while True:
        current_count = Facility.objects.count()
        
        if current_count != previous_count:
            print(f"\n{'='*70}")
            print(f"🔔 CHANGE DETECTED! Count changed from {previous_count} to {current_count}")
            print(f"{'='*70}\n")
            
            # Show all facilities
            all_facilities = Facility.objects.all().order_by('-id')
            
            print("Current facilities in database:")
            for f in all_facilities:
                print(f'\n  ID: {f.id}')
                print(f'  Name: {f.name}')
                print(f'  Type: {f.location_type}')
                print(f'  Gender: {f.gender}')
                print(f'  Block: {f.block}, Floor: {f.floor}')
            
            print(f"\n{'='*70}\n")
            previous_count = current_count
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Current count: {current_count} facilities (no change)", end='\r')
        
        time.sleep(3)
        
except KeyboardInterrupt:
    print("\n\nMonitoring stopped.")
    print(f"Final count: {Facility.objects.count()} facilities")
