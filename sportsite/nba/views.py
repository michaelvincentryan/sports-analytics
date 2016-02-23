from django.shortcuts import render, get_object_or_404
from nba.models import Team, Standings
import datetime

# Create your views here.
#from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def teams(request):
    teams = Team.objects.all().order_by('-division__conference','division')
    return render(request, 'teams.html', {'teams':teams,})

def team(request, team):
    team = get_object_or_404(Team, nickname=team)
    return render(request, 'team.html', {'team':team,})

def standings(request):
    eastern_standings = Standings.objects.filter(date__year="2016", team__division__conference=1).order_by('-pct')
    western_standings = Standings.objects.filter(date__year="2016", team__division__conference=2).order_by('-pct')
    return render(request, 'standings.html', {'eastern_standings':eastern_standings,
                                              'western_standings':western_standings,})
