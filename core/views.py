from django.shortcuts import render
import requests
import time 
import random
import json

from .models import Player

# admin section (to add functionality later)

def player_data(request):
    milestones=[]
    player_former_teams=[]
    player_data=[]


    # #former teams using player ids , which can apply(ids) when looking up players
    former_teams=f"https://www.thesportsdb.com/api/v1/json/123/lookupformerteams.php?id=34146370"
    milestones="https://www.thesportsdb.com/api/v1/json/123/lookupmilestones.php?id=34161397"
    statistics="https://www.thesportsdb.com/api/v1/json/123/lookupplayerstats.php?id=34146304"
    team_players="https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604"

    # handling the search player data

    if request.method == 'POST':

        player_name = request.POST.get('player_search', '').strip()

        if not player_name:
            return render(request, 'index.html', {
                'error': 'Please enter a player name.'
            })

        url = 'https://www.thesportsdb.com/api/v1/json/123/searchplayers.php'

        try:
            response = requests.get(
                url,
                params={'p': player_name},
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            players = data.get('player')

            if not players:
                return render(request, 'index.html', {
                    'error': 'Player not found.'
                })

            general_info = players[0]

            player, created = Player.objects.update_or_create(
                player_id=general_info.get('idPlayer'),
                defaults={
                    'name': general_info.get('strPlayer') or '',
                    'nationality': general_info.get('strNationality') or '',
                    'photo': general_info.get('strCutout') or '',
                }
            )

            message = 'Player added successfully!' if created else 'Player information updated!'

            return render(request, 'index.html', {
                'player': player,
                'message': message
            })

        except requests.RequestException as e:
            return render(request, 'index.html', {
                'error': f'API connection error: {e}'
            })

        except ValueError:
            return render(request, 'index.html', {
                'error': 'Could not read the API response.'
            })

    return render(request, 'index.html')
   


def team_data(request):
    return render(request,'team.html')


def randomizer(request):
    players=Player.objects.all()

    # converts the list of all players and selects one at ranmdom
    if players.exists():
        player=random.choice(list(players))

    else:
        player=None

    return render(request,'players.html',{'player':player})

def answer_checker(request):
    if request.method=='POST':
        answer=request.POST.get('player_answer')

    if not answer:
        return render(request, 'index.html', {
            'error': 'Please enter a player name.'
        })
    return render(request,'players.html')