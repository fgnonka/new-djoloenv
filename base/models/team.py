from django.db import models
from .country import Country
from django.utils.text import slugify
from django.urls import reverse


class Team(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False)
    year = models.IntegerField()
    slug = models.SlugField(max_length=55, unique=True,
                            help_text="Label for URL configuration", null=True, blank=True)
        
    def __str__(self):
        return f'{self.country} --- {self.year}'
    

    def save(self, *args, **kwargs): 
        value = self.country.name + "-" + str(self.year)# new
        if not self.slug:
            self.slug = slugify(value, allow_unicode=True)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['year']