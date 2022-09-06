from django.contrib import admin
from .models.country import Country
from .models.player import Player
from .models.playercard import PlayerCard
from .models.portfolio import Portfolio
from .models.rarity import Rarity
from .models.team import Team

# Imports to extract specific values from foreignkeys

#Prepopulated fields for SlugFields and URL mapping

# Register your models here.
admin.site.register(Country)
admin.site.register(Player)
admin.site.register(PlayerCard)
admin.site.register(Portfolio)
admin.site.register(Rarity)
admin.site.register(Team)


