from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def index(request):

    return render(request, 'armada/index.html')

@login_required
def userdashboard(request):
    return render(request, 'armada/userdashboard.html')

@login_required
def create(request):
    return render(request, 'armada/create.html')