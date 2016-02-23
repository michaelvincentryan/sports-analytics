from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teams/(?P<team>\w+)', views.team, name='team'),
    url(r'^teams', views.teams, name='teams'),
    url(r'^standings', views.standings, name='standings'),
    url(r'^', views.home, name='nba_home'),
]
