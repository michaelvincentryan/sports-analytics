from django.contrib import admin

# Register your models here.
from models import Team, Standings, Conference, Division

admin.site.register(Team)
admin.site.register(Standings)
admin.site.register(Conference)
admin.site.register(Division)
