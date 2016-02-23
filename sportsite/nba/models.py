from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Conference(models.Model):
    conferences = (
        ('E', 'Eastern'),
        ('W', 'Western'),
    )

    name = models.CharField(max_length = 50, choices=conferences)

    def __unicode__(self):
        return self.name

class Division(models.Model):
    divisions = (
        ('A', 'Atlantic'),
        ('C', 'Central'),
        ('SE', 'Southeast'),
        ('P', 'Pacific'),
        ('NW', 'Northwest'),
        ('SW', 'Southwest'),
    )

    name = models.CharField(max_length = 50, choices=divisions)
    conference = models.ForeignKey(Conference)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    division = models.ForeignKey(Division, default=1)

    def __unicode__(self):
        return self.name + " " + self.nickname

class Standings(models.Model):
    date = models.DateTimeField()
    team = models.ForeignKey(Team)
    wins = models.IntegerField()
    losses = models.IntegerField()
    pct = models.DecimalField(max_digits =  3, decimal_places = 3)
    gb = models.DecimalField(max_digits =  3, decimal_places = 1)
    home_wins = models.IntegerField()
    home_losses = models.IntegerField()
    road_wins = models.IntegerField()
    road_losses = models.IntegerField()
    division_wins = models.IntegerField()
    division_losses = models.IntegerField()
    conference_wins = models.IntegerField()
    conference_losses = models.IntegerField()
    ppg = models.DecimalField(max_digits =  4, decimal_places = 1)
    opp_ppg = models.DecimalField(max_digits =  4, decimal_places = 1)
    pt_diff = models.DecimalField(max_digits =  4, decimal_places = 1)
    win_streak = models.IntegerField()
    last_10_wins = models.IntegerField()
    last_10_losses = models.IntegerField()

    def __unicode__(self):
        return self.team.nickname + ": " + str(self.wins) + "-" + str(self.losses)

    class Meta:
        verbose_name_plural = "Standings"
