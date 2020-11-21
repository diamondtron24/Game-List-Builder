from django.urls import path
from . import views

app_name = "armada"
urlpatterns = [
    path('', views.index, name="index"),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('create/', views.create, name='create'),
    path('create/getBaseShips/<str:faction>/', views.getBaseShips, name='getBaseShips'),
]