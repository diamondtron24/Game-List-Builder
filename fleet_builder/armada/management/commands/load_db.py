from django.core.management.base import BaseCommand
import json
from armada.models import Ship


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('ships.json') as file:

            shipdata = json.load(file)
        
        for ship in shipdata:
            vessel = Ship()
            vessel.title=ship['title']
            vessel.image= ''
            vessel.card_type=ship['set']
            vessel.ship_type=ship['type']
            vessel.points=ship['points']
            vessel.faction=ship['faction']
            vessel.size=ship['size']
            vessel.commander=ship['upgrades'].get('commander', False)
            vessel.officer_1=ship['upgrades'].get('officer', False)
            vessel.officer_2=ship['upgrades'].get('officer-2', False)
            vessel.officer_3=ship['upgrades'].get('officer-3', False)
            vessel.officer_4=ship['upgrades'].get('officer-4', False)
            vessel.fleet_command_1=ship['upgrades'].get('fleet-command', False)
            vessel.fleet_command_2=ship['upgrades'].get('fleet-command-2', False)
            vessel.fleet_command_3=ship['upgrades'].get('fleet-command-3', False)
            vessel.fleet_command_4=ship['upgrades'].get('fleet-command-4', False)
            vessel.offensive_retrofit_1=ship['upgrades'].get('offensive-retrofit', False)
            vessel.offensive_retrofit_2=ship['upgrades'].get('offensive-retrofit-2', False)
            vessel.defensive_retrofit_1=ship['upgrades'].get('defensive-retrofit', False)
            vessel.defensive_retrofit_2=ship['upgrades'].get('defensive-retrofit-2', False)
            vessel.turbolasers_1=ship['upgrades'].get('turbolasers', False)
            vessel.turbolasers_2=ship['upgrades'].get('turbolasers-2', False)
            vessel.ion_cannons_1=ship['upgrades'].get('ion-cannons', False)
            vessel.ion_cannons_2=ship['upgrades'].get('ion-cannons-2', False)
            vessel.ordinance_1=ship['upgrades'].get('ordinance', False)
            vessel.ordinance_2=ship['upgrades'].get('ordinance-2', False)
            vessel.support_team_1=ship['upgrades'].get('support-team', False)
            vessel.support_team_2=ship['upgrades'].get('support-team-2', False)
            vessel.weapons_team_1=ship['upgrades'].get('weapons-team', False)
            vessel.weapons_team_2=ship['upgrades'].get('weapons-team-2', False)
            vessel.experimental_retrofit_1=ship['upgrades'].get('experimental-retrofit', False)
            vessel.experimental_retrofit_2=ship['upgrades'].get('experimental-retrofit-2', False)
            vessel.super_weapon=ship['upgrades'].get('super-weapon', False)
            vessel.upgrade_title=ship['upgrades'].get('title', False)
            vessel.save()
            