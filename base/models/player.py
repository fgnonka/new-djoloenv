from django.db import models
from .team import Team
from .country import Country
from django.utils.text import slugify


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    jersey_number = models.CharField(max_length=10)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=55,
                            help_text="Label for URL configuration", null=True, blank=True)

    def __str__(self):
        return f'{self.name} --- {self.position} --- {self.team}'
    
    @staticmethod
    def get_all_players_by_team(team):
        if team:
            return Player.objects.filter(team=team)
        else:
            return None
    
    def save(self, *args, **kwargs): 
        value = self.name + "-" + str(self.team.country.name)# new
        if not self.slug:
            self.slug = slugify(value, allow_unicode=False)
        return super().save(*args, **kwargs)