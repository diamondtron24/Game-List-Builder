from django.core.management.base import BaseCommand

from armada.models import Objective
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        Objective.objects.all().delete()
        
        with open('objectives.csv', 'r') as file:

            reader = csv.reader(file, delimiter = '|')
            for row in list(reader)[1:]:
                objective = Objective()
                objective.title = row[1].strip()
                objective.image = row[2].strip()
                objective.objective_type = row[3].strip()
                objective.setup = row[4].strip()
                objective.special_rule = row[5].strip()
                objective.end_of_round = row[6].strip()
                objective.end_of_game = row[7].strip()
                objective.score = row[8].strip()

                print(objective)
                objective.save()