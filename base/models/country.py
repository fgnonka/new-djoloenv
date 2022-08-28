from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, unique = True)
    
    class Meta: 
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name