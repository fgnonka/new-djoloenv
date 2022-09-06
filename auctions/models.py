from django.db import models
from django.urls import reverse
from user_account.djolouser import DjolowinUser
from trades.models import OwnedCard
from django_prices.models import MoneyField


# Create your models here.

class AuctionedCard(models.Model):
    owner = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    card = models.ForeignKey(OwnedCard, on_delete=models.CASCADE)
    duration = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    starting_bid = MoneyField(
        amount_field="starting_bid", currency_field="DJOL"
    )
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Auction #{self.id}: {self.card}"
    
    def get_absolute_url(self):
        return reverse("auctions:auction-detail", kwargs={"pk": self.pk})
    
    
class Bid(models.Model):
    owner = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    listed_card = models.ForeignKey(AuctionedCard, on_delete=models.CASCADE)
    bid = MoneyField(
        amount_field="actual_bid", currency_field="DJOL"
    )
    
class AuctionWinner(models.Model):
    winning_bid = models.ForeignKey(Bid, on_delete=models.CASCADE)