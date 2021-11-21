from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from Home.models import Champion
import json
# from rest_framework.request import Request
import requests

from Home.serializers import ChampionSerializer


# from Home.serializers import ChampionSerializer (include this again when you use uncomment ChampionSerializer from serializers.py)


# Create your views here.
API_KEY = 'RGAPI-0e5897b4-baa0-45be-9ad5-d3722a753868'
BASE_URL = 'https://na1.api.riotgames.com'


# f = open('D:\Github\CSDBackend\LeagueProBackend\Home\champion.json', encoding='utf-8')

# motherload = json.load(f) # this loads the entire json file onto motherload
# championData = motherload['data']#this loads only the data on teh champions onto placeholder
# f.close()

@csrf_exempt
def testSummonerAPI(request):
    

    #summoner portion
    summonerResponse = requests.get(BASE_URL + '/lol/summoner/v4/summoners/by-name/KingSwirly' + '?api_key=' + API_KEY)
    summonerInfo = summonerResponse.json()

    name = summonerInfo['name']
    id = summonerInfo['id']
    summonerLevel = summonerInfo['summonerLevel']


    #champion portion
    championResponse = requests.get(BASE_URL+ '/lol/champion-mastery/v4/champion-masteries/by-summoner/Nvf9hmdO4Z-pObFxwZG4hIBZOVmT62VvbX3EetuLz41gOZY' + API_KEY)
    championsInfo = championResponse.json()
    


    return JsonResponse({
        'summonerName': name, 
        'summonerLevel': summonerLevel}, 
        safe=False)

@csrf_exempt
def SummonerAPI(request, summonerName):
    
    #Summoners

    summonerResponse = requests.get(BASE_URL + '/lol/summoner/v4/summoners/by-name/'+ summonerName + '?api_key=' + API_KEY)
    summonerInfo = summonerResponse.json()

    name = summonerInfo['name']
    id = summonerInfo['id']
    summonerLevel = summonerInfo['summonerLevel']




    #Champions
    championResponse = requests.get(BASE_URL + '/lol/champion-mastery/v4/champion-masteries/by-summoner/'+ id + '?api_key=' + API_KEY)
    championInfo = championResponse.json()
    champion1 = championInfo[1] 
    champion2 = championInfo[2]
    champion3 = championInfo[3]



    champion1key = champion1['championId']
    champion2key = champion2['championId']
    champion3key = champion3['championId']

    #querying the database for the champion's name by using the championKey. 
    #the championKey is the championId obtained from a RIOT API query
    #the championKey from RIOT API is a Long data type, and needs to be compared with int data types in the database
    #after that, just extract the corresponding championName. 
    #On second thought, it looks like i tried to serialize the championKey back into json, when that's not necessary. I just need the name. Look into this next?
    # champion1keydb = Champion.objects.all().filter(int(champion1key))
    # champion1json = ChampionSerializer(champion1keydb)
    # champion2keydb = Champion.objects.all().filter(int(champion2key))
    # champion2json = ChampionSerializer(champion2keydb)
    # champion3keydb = Champion.objects.all().filter(int(champion3key))
    # champion3json = ChampionSerializer(champion3keydb)



    #THIS IS FOR TRYING TO EXTRACT SHIT FROM THE DATA DRAGON < FAILED METHOD
    # for key,value in championData.items():
        
    #     if(champion1key == championData[value]['key']):
    #         champion1Name = championData[value]['name']
    #     if(champion2key == championData[value]['key']):
    #         champion2Name = championData[value]['name']
    #     if(champion3key == championData[value]['key']):
    #         champion3Name = championData[value]['name']
        
    



    champion1Level = champion1['championLevel']
    champion2Level = champion2['championLevel']
    champion3Level = champion3['championLevel']

    champion1Points = champion1['championPoints']
    champion2Points = champion2['championPoints']
    champion3Points = champion3['championPoints']
    
    return JsonResponse({
        'summonerName': name, 
        'summonerLevel': summonerLevel,
        # 'championName' : [ champion1json, champion2json, champion3json ],
        'championLevel' : [ champion1Level, champion2Level, champion3Level ],
        'championPoints' : [ champion1Points, champion2Points, champion3Points ]
        }, 
        safe=False)
