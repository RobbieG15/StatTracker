from django.contrib import admin
from .models import User, Organization, Team, Player

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(Player)