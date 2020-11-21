from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ship, Squadron, Objective, SavedList, BaseShip, Upgrade


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

        # print(base_ships)
    return JsonResponse({'base_ships': base_ship_output})