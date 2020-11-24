from django.urls import path
from . import views

app_name = "armada"
urlpatterns = [
    path('', views.index, name="index"),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('create/', views.create, name='create'),
    path('create/getBaseShips/<str:faction>/', views.getBaseShips, name='getBaseShips'),
    path('create/getSingleShip/<int:ship_id>/', views.getSingleShip, name='getSingleShip'),
    path('create/saveShip/<str:save_ship>/', views.saveShip, name='saveShip'),
]