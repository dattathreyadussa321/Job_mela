from django.core.management.base import BaseCommand
from companies.models import Facility


class Command(BaseCommand):
    help = 'Clear ALL toilets from the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm deletion of all toilets'
        )

    def handle(self, *args, **options):
        toilets = Facility.objects.filter(location_type='TOILET')
        count = toilets.count()
        
        if count == 0:
            self.stdout.write(self.style.WARNING('No toilets to delete.'))
            return
        
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(f'⚠️  This will delete {count} toilet(s)!')
            )
            self.stdout.write(
                self.style.WARNING('Run with --confirm to proceed')
            )
            return
        
        toilets.delete()
        self.stdout.write(
            self.style.SUCCESS(f'✅ Deleted {count} toilet(s)')
        )
