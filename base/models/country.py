from django_countries.fields import CountryField
from django.db import models

class Country(models.Model):
    name = CountryField()

    
    class Meta: 
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name