from django.core.management.base import BaseCommand
from companies.models import Facility


class Command(BaseCommand):
    help = 'Add a new toilet/restroom to the database'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, required=True, help='Name of the restroom')
        parser.add_argument('--gender', type=str, required=True, choices=['MALE', 'FEMALE'], help='Gender (MALE or FEMALE)')
        parser.add_argument('--block', type=str, required=True, help='Block (e.g., A, B, C)')
        parser.add_argument('--floor', type=int, required=True, help='Floor number (e.g., 0, 1, 2)')
        parser.add_argument('--room', type=str, required=False, help='Room number (optional)')

    def handle(self, *args, **options):
        name = options['name']
        gender = options['gender']
        block = options['block']
        floor = options['floor']
        room = options.get('room', '')

        # Create the toilet
        toilet = Facility.objects.create(
            name=name,
            location_type='TOILET',
            gender=gender,
            block=block,
            floor=floor,
            room_number=room if room else None
        )

        self.stdout.write(
            self.style.SUCCESS(f'✅ Successfully added toilet: {toilet.name}')
        )
        self.stdout.write(f'   Gender: {toilet.get_gender_display()}')
        self.stdout.write(f'   Location: Block {toilet.block}, Floor {toilet.floor}')
        
        total = Facility.objects.filter(location_type='TOILET').count()
        self.stdout.write(self.style.SUCCESS(f'\n📊 Total toilets in database: {total}'))
