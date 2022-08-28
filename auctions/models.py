from django.db import models
from django.urls import reverse
from base.models.djolouser import DjolowinUser
from base.models.playercard import PlayerCard
from base.models.portfolio import Portfolio

# Create your models here.

class AuctionList(models.Model):
    owner = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    card = models.ForeignKey(PlayerCard, on_delete=models.CASCADE)
    duration = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    starting_bid = models.IntegerField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Auction #{self.id}: {self.card}"
    
    def get_absolute_url(self):
        return reverse("auctions:auction-detail", kwargs={"pk": self.pk})
    
    
class Bid(models.Model):
    owner = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    listed_item = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    bid = models.IntegerField()
    
class AuctionWinner(models.Model):
    winning_bid = models.ForeignKey(Bid, on_delete=models.CASCADE)