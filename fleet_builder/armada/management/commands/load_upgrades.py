from django.core.management.base import BaseCommand

from armada.models import Upgrade
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        Upgrade.objects.all().delete()
        
        with open('upgrades copy.csv', 'r') as file:

            reader = csv.reader(file, delimiter = ',')
            for row in list(reader)[1:]:
                upgrade = Upgrade()
                upgrade.title = row[1].strip()
                upgrade.image = row[2].strip()
                upgrade.upgrade_type = row[3].strip()
                upgrade.points = row[4].strip()
                upgrade.faction = row[5].strip()
                upgrade.unique = bool(row[6].strip())
                upgrade.ship = row[7].strip()
                upgrade.ships = row[8].strip()
                upgrade.dual = row[9].strip()
                upgrade.modification = bool(row[10].strip())

                print(upgrade)
                upgrade.save()