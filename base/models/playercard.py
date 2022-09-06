from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from .player import Player
from .rarity import Rarity


class PlayerCard(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True, blank=True)
    rarity = models.ForeignKey(
        Rarity, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='uploads/cards', null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=55, unique=True, blank=True)

    def __str__(self):
        return f'{self.player} --- {self.rarity} --- {self.index}'
    
    def get_absolute_url(self):
        return reverse("base:playercard", kwargs={
            "slug": self.slug
            })
        
    
    @staticmethod
    def get_all_cards():
        return PlayerCard.objects.all()
    
    @staticmethod
    def get_all_cards_by_player(player):
        if player:
            return PlayerCard.objects.filter(player=player)
        else:
            return PlayerCard.objects.all()
        
    def save(self, *args, **kwargs): 
        value = self.player.name + "-" + self.rarity.name + '-' + self.player.team.country.name + '-' + str(self.index)# new
        if not self.slug:
            self.slug = slugify(value, allow_unicode=False)
        return super().save(*args, **kwargs)