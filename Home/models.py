from django.db import models

class Champion(models.Model):
    ChampionName = models.CharField(max_length=20)
    ChampionKey = models.IntegerField(default = 999)
