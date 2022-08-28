from django.contrib import admin
from .models import AuctionList, Bid, AuctionWinner
# Register your models here.

admin.site.register(AuctionList)
admin.site.register(Bid)
admin.site.register(AuctionWinner)
