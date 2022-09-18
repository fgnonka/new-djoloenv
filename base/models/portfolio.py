from django.db import models
from user_account.djolouser import DjolowinUser

class Portfolio(models.Model):
    owner = models.OneToOneField(
        DjolowinUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Portfolio of {self.owner}'
    
    