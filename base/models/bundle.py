from django.db import models
from .playercard import PlayerCard
# Create your models here.

class Bundle(models.Model):
    name = models.CharField(max_length=255)
    cards = models.ManyToManyField(
        PlayerCard, blank=True, related_name='bundle_cards')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
