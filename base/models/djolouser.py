from django.db import models
from django.contrib.auth.models import User


class DjolowinUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True, blank=True)
    account_balance = models.IntegerField(default=0)
    country = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    joined_on = models.DateField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='uploads/profiles', default='base/img/avatar-default.jpg')    
    
    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return DjolowinUser.objects.get(email=email)
        except:
            return False
    
    def isExists(self):
        if DjolowinUser.objects.filter(email=self.email):
            return True
        return False
    
    def __str__(self) -> str:
        return 'User #' + str(self.id) +': ' + self.username