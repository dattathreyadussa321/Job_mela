from django.core.management.base import BaseCommand
from companies.models import Facility


class Command(BaseCommand):
    help = 'List all toilets in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--gender',
            type=str,
            choices=['MALE', 'FEMALE'],
            required=False,
            help='Filter by gender'
        )
        parser.add_argument(
            '--block',
            type=str,
            required=False,
            help='Filter by block'
        )

    def handle(self, *args, **options):
        toilets = Facility.objects.filter(location_type='TOILET')
        
        # Apply filters
        if options.get('gender'):
            toilets = toilets.filter(gender=options['gender'])
        if options.get('block'):
            toilets = toilets.filter(block=options['block'])
        
        # Display results
        self.stdout.write(self.style.SUCCESS(f'\n{"="*70}'))
        self.stdout.write(self.style.SUCCESS(f'🚻 RESTROOMS DATABASE'))
        self.stdout.write(self.style.SUCCESS(f'{"="*70}\n'))
        
        if not toilets.exists():
            self.stdout.write(self.style.WARNING('No toilets found matching the criteria.'))
            return
        
        self.stdout.write(f'Total: {toilets.count()} restroom(s)\n')
        
        for toilet in toilets:
            icon = '🚹' if toilet.gender == 'MALE' else '🚺'
            self.stdout.write(f'{icon} {toilet.name}')
            self.stdout.write(f'   ID: {toilet.id}')
            self.stdout.write(f'   Gender: {toilet.get_gender_display()}')
            self.stdout.write(f'   Location: Block {toilet.block}, Floor {toilet.floor}')
            if toilet.room_number:
                self.stdout.write(f'   Room: {toilet.room_number}')
            self.stdout.write('')
        
        self.stdout.write(self.style.SUCCESS(f'{"="*70}'))
