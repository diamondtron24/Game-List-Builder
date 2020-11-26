from django.db import models

# Create your models here.

class BaseShip(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    ship_type = models.CharField(max_length=50)
    points = models.IntegerField()
    faction = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    commander = models.BooleanField(default=False)
    officer_1 = models.BooleanField(default=False)
    officer_2 = models.BooleanField(default=False)
    officer_3 = models.BooleanField(default=False)
    officer_4 = models.BooleanField(default=False)
    fleet_command_1 = models.BooleanField(default=False)
    fleet_command_2 = models.BooleanField(default=False)
    fleet_command_3 = models.BooleanField(default=False)
    fleet_command_4 = models.BooleanField(default=False)
    
    offensive_retrofit_1 = models.BooleanField(default=False)
    offensive_retrofit_2 = models.BooleanField(default=False)
    defensive_retrofit_1 = models.BooleanField(default=False)
    defensive_retrofit_2 = models.BooleanField(default=False)
    turbolasers_1 = models.BooleanField(default=False)
    turbolasers_2 = models.BooleanField(default=False)
    ion_cannons_1 = models.BooleanField(default=False)
    ion_cannons_2 = models.BooleanField(default=False)
    ordinance_1 = models.BooleanField(default=False)
    ordinance_2 = models.BooleanField(default=False)
    support_team_1 = models.BooleanField(default=False)
    support_team_2 = models.BooleanField(default=False)
    weapons_team_1 = models.BooleanField(default=False)
    weapons_team_2 = models.BooleanField(default=False)
    experimental_retrofit_1 = models.BooleanField(default=False)
    experimental_retrofit_2 = models.BooleanField(default=False)
    super_weapon = models.BooleanField(default=False)
    upgrade_title  = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Squadron(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    squad_type = models.CharField(max_length=50)
    points = models.IntegerField()
    faction = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    unique = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Upgrade(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    upgrade_type = models.CharField(max_length=50)
    points = models.IntegerField()
    faction = models.CharField(max_length=50)
    unique = models.BooleanField(default=False)
    ship = models.CharField(max_length=50)
    ships = models.CharField(max_length=50)
    dual = models.CharField(max_length=50)
    modification = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Objective(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    objective_type = models.CharField(max_length=50, blank=True, null=True)
    setup = models.TextField(blank=True, null=True)
    special_rule = models.TextField(blank=True, null=True)
    end_of_round = models.TextField(blank=True, null=True)
    end_of_game = models.TextField(blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Ship(models.Model):
    title = models.CharField(max_length=50)
    ship = models.ManyToManyField(BaseShip, related_name="saved_ship")
    upgrades = models.ManyToManyField(Upgrade, related_name="ships_including_these_upgrades")
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SavedList(models.Model):
    fleet_name = models.CharField(max_length=50)
    fleet = models.ManyToManyField(Ship, related_name="fleet")
    squadrons = models.ManyToManyField(Squadron, related_name="fleet")
    objectives = models.ManyToManyField(Objective, related_name='fleet')
    
    def __str__(self):
        return self.fleet_name

class UpgradeImage(models.Model):
    upgrade_type = models.CharField(max_length=50)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.upgrade_type
