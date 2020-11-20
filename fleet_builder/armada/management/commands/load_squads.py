from django.core.management.base import BaseCommand

from armada.models import Squadron
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        Squadron.objects.all().delete()
        
        with open('squads.csv', 'r') as file:

            reader = csv.reader(file, delimiter = '|')
            for row in list(reader)[1:]:
                squadron = Squadron()
                squadron.title = row[1].strip()
                squadron.image = row[2].strip()
                squadron.card_type = row[3].strip()
                squadron.squad_type = row[4].strip()
                squadron.points = row[5].strip()
                squadron.faction = row[6].strip()
                squadron.keywords = row[7].strip()
                squadron.unique = bool(row[8].strip())

                squadron.save()