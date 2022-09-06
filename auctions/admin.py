from django.contrib import admin
from .models import (AuctionedCard, Bid, AuctionWinner)
# Register your models here.

admin.site.register(AuctionedCard)
admin.site.register(Bid)
admin.site.register(AuctionWinner)
