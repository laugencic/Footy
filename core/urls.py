from django.urls import path
from . import views

urlpatterns=[
    path('',views.player_data,name="index"),
    path('teams/',views.team_data,name="teams"),
    path('players/',views.randomizer,name='players')
]