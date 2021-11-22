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

    sumName = str('name')
    sumId = summonerInfo['id']
    sumLevel = summonerInfo['summonerLevel']




    # Champions
    championResponse = requests.get(BASE_URL + '/lol/champion-mastery/v4/champion-masteries/by-summoner/' + sumId + '?api_key=' + API_KEY)
    championInfo = championResponse.json()
    champion1 = championInfo[0]
    champion2 = championInfo[1]
    champion3 = championInfo[2]

    f = open('./resources/champion.json', encoding="utf-8")
    championDetails = json.loads(f.read())

    champion1key = champion1['championId']
    champion2key = champion2['championId']
    champion3key = champion3['championId']

    champion1name = "None"
    champion2name = "None"
    champion3name = "None"

    for champ in championDetails['data']:
        if championDetails['data'][champ]['key'] == str(champion1key):
            champion1name = champ
        if championDetails['data'][champ]['key'] == str(champion2key):
            champion2name = champ
        if championDetails['data'][champ]['key'] == str(champion3key):
            champion3name = champ


    champion1Level = champion1['championLevel']
    champion2Level = champion2['championLevel']
    champion3Level = champion3['championLevel']

    champion1Points = champion1['championPoints']
    champion2Points = champion2['championPoints']
    champion3Points = champion3['championPoints']
    
    return JsonResponse({
        'summonerName': sumName,
        'summonerLevel': sumLevel,
        'championName': [champion1name, champion2name, champion3name],
        'championLevel': [champion1Level, champion2Level, champion3Level],
        'championPoints': [champion1Points, champion2Points, champion3Points]
        }, 
        safe=False)
