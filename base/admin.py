from django.contrib import admin
from .models.bundle import Bundle
from .models.country import Country
from .models.orders import CardOrder, BundleOrder
from .models.player import Player
from .models.playercard import PlayerCard
from .models.portfolio import Portfolio
from .models.rarity import Rarity
from .models.team import Team
from .models.djolouser import DjolowinUser

# Imports to extract specific values from foreignkeys

#Prepopulated fields for SlugFields and URL mapping

# Register your models here.
admin.site.register(Bundle)
admin.site.register(Country)
admin.site.register(CardOrder)
admin.site.register(BundleOrder)
admin.site.register(Player)
admin.site.register(PlayerCard)
admin.site.register(Portfolio)
admin.site.register(Rarity)
admin.site.register(Team)
admin.site.register(DjolowinUser)


