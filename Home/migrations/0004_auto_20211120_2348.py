# Generated by Django 3.2.7 on 2021-11-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20211120_1102'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Summoner',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('summonerName', models.JSONField()),
        #         ('summonerLevel', models.JSONField()),
        #         ('ChampionName', models.JSONField()),
        #         ('ChampionLevel', models.JSONField()),
        #         ('ChampionPoints', models.JSONField()),
        #         ('ChampionId', models.JSONField()),
        #     ],
        # ),
        migrations.RemoveField(
            model_name='champion',
            name='ChampionPortrait',
        ),
        # migrations.RemoveField(
        #     model_name='champion',
        #     name='id',
        # ),
        # migrations.AddField(
        #     model_name='champion',
        #     name='ChampionID',
        #     field=models.AutoField(default=999, primary_key=True, serialize=False),
        # ),
        # migrations.AlterField(
        #     model_name='champion',
        #     name='ChampionKey',
        #     field=models.IntegerField(default=999),
        # ),
    ]