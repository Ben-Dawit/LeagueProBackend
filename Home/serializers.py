
from rest_framework import serializers
from Home.models import Champion

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ('ChampionName', 'ChampionKey')

