from django.db import models


class Rarity(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def get_all_rarities():
        return Rarity.objects.all()

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']
        verbose_name = 'Rarity'
        verbose_name_plural = 'Rarities'
    
    # @property
    # def count_active_auctions(self):
    #     return Auction.objects.filter(category=self).count()