from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ship, Squadron, Objective, SavedList, BaseShip, Upgrade, UpgradeImage
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt    


# Create your views here.

def index(request):

    return render(request, 'armada/index.html')

@login_required
def userdashboard(request):
    return render(request, 'armada/userdashboard.html')

@login_required
def create(request):
    return render(request, 'armada/create.html')


def getBaseShips(request, faction):
    base_ships = BaseShip.objects.filter(faction=faction)
    base_ship_output = []
    
    for ship in base_ships:
        base_ship_output.append({
            'key': ship.id,
            'ship_title': ship.title,
            'ship_image': ship.image
        })
        ship_out = ''
        # print(base_ship_output)
    return JsonResponse({'base_ships': base_ship_output,})

def getSingleShip(request, ship_id):
    ship = BaseShip.objects.get(pk = ship_id)
    ship_stats = model_to_dict(ship)
    upgrade_faction = ship.faction 
    upgrade_image = UpgradeImage.objects.all()
    avail_upgrades = []
    upgrades = Upgrade.objects.filter(faction = upgrade_faction) | Upgrade.objects.filter(faction = 'nuetral')
    upgrades = list(upgrades)

    for key in ship_stats:
        if ship_stats[key] == True:
            for upgrade in upgrades:
                if upgrade.upgrade_type in key.replace('_', ' '):
                    ship_upgrade = model_to_dict(upgrade)
                    for image in upgrade_image:
                        if image.upgrade_type in key:
                            ship_upgrade['upgrade_icon'] = model_to_dict(image)
                    avail_upgrades.append(ship_upgrade)


    return JsonResponse({'ship' : ship_stats, 'upgrades':avail_upgrades})

@csrf_exempt
def saveShip(request):

    print(request.body)
    
    return redirect('armada:create')




    