# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import urllib2
from bs4 import BeautifulSoup

def populate_team_names(apps, schema_editor):
    Team = apps.get_model("nba", "Team")

    url = 'http://espn.go.com/nba/standings'

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    rows = soup.select('.standings-row')

    for row in rows:
        row_soup = BeautifulSoup(str(row))
        team_name = row_soup.select('.team-names')[0].string
        team_name = team_name.rpartition(' ') #returns a 3-tuple with the second
        #element being the partition (' ')
        name = team_name[0]
        nickname = team_name[2]
        team = Team(name=name, nickname=nickname)
        team.save()

class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_team_names),
    ]
