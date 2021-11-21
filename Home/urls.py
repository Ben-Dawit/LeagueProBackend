from django.conf.urls import url
from Home import views

urlpatterns = [
    
    url(r'^summoner$',views.testSummonerAPI),
    url(r'^summoner/(?P<summonerName>\w+)',views.SummonerAPI)
]

