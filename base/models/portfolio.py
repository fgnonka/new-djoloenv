from django.db import models
from user_account.djolouser import DjolowinUser
from base.models.playercard import PlayerCard
from trades.models import OwnedCard

class Portfolio(models.Model):
    owner = models.OneToOneField(
        DjolowinUser, on_delete=models.CASCADE, null=True, blank=True)
    cards = models.ManyToManyField(PlayerCard)

    def __str__(self):
        return f'Portfolio of {self.owner}'
    
    # def change_to_owned_cards(self):
    #     if self.cards:
    #         for i in self.cards:
    #             OwnedCard.objects.create(owner=self.owner, card=i)