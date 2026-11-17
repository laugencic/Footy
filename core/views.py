from django.shortcuts import render
import requests
import time 
import random
import json


def data(request):
    # #former teams using player ids , which can apply(ids) when looking up players
    former_teams=f"https://www.thesportsdb.com/api/v1/json/123/lookupformerteams.php?id=34146370"
    milestones="https://www.thesportsdb.com/api/v1/json/123/lookupmilestones.php?id=34161397"
    statistics="https://www.thesportsdb.com/api/v1/json/123/lookupplayerstats.php?id=34146304"
    team_players="https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604"
    player=f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p=Lionel Messi"

    sample= [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kevin De Bruyne",
    "Johan Cruyff"
   
    ]

    # request1=requests.get(player)

    # player_random_info=request1.json()
    # general_info=player_random_info['player'][0]

    # player_data={
    #     'name':general_info.get('strPlayer'),
    #     'player_id':general_info.get('idPlayer'),
    #     'nationality':general_info.get('strNationality'),
    #     'image':general_info.get('strCutout')

    # }
    
    # Extracting the former team information
    request2=requests.get(former_teams)
    # print(request2.json())

    random_team_info=request2.json()
    former_teams=random_team_info['formerteams']

    # for team in former_teams:
        # for key,value in team.items():
        #     if key=='strFormerTeam':
        #         print("former teams",value)



    # milestones
    request3=requests.get(milestones)
    print(request3.json())
    return render(request,'index.html')

