from django.core.management.base import BaseCommand
from companies.models import Facility


class Command(BaseCommand):
    help = 'Delete a toilet by ID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID of the toilet to delete')

    def handle(self, *args, **options):
        toilet_id = options['id']
        
        try:
            toilet = Facility.objects.get(id=toilet_id, location_type='TOILET')
            name = toilet.name
            toilet.delete()
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Successfully deleted: {name}')
            )
            
            total = Facility.objects.filter(location_type='TOILET').count()
            self.stdout.write(f'📊 Remaining toilets: {total}')
            
        except Facility.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'❌ Toilet with ID {toilet_id} not found')
            )
