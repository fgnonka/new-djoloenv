from django.db import models
from django.conf import settings
from django.db.models import JSONField  # type: ignore
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string
from django.forms.models import model_to_dict
from django.utils import timezone
from . import CustomerEvents
from core.json_serializer import CustomJsonEncoder



class DjolowinUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()
    country = CountryField()
    phone = PhoneNumberField()
    profile_pic = models.ImageField(upload_to='uploads/profiles', default='base/img/avatar-default.jpg')
    jwt_token_key = models.CharField(max_length=12, default=get_random_string(length=22))    
    account_balance = models.IntegerField(default=0)
    joined_on = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    language_code = models.CharField(
        max_length=35, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE
    )
    
    USERNAME_FIELD = "username"
    
    class Meta:
        ordering = ("username",)
    
    def register(self):
        self.save()
        
    def get_full_name(self):
        if self.first_name or self.last_name:
            return ("%s %s" % (self.first_name, self.last_name)).strip()
        return self.email
    
    def get_email(self):
        return self.email

    def get_username(self) -> str:
        return self.username
    
    @staticmethod
    def get_user_by_username(username):
        try:
            return DjolowinUser.objects.get(username=username)
        except:
            return False
    
    def isExists(self):
        if DjolowinUser.objects.filter(username=self.username):
            return True
        return False
    
    def __str__(self) -> str:
        return 'User #' + str(self.id) +': ' + self.username
    

class CustomerEvent(models.Model):
    """Model used to store events that happened during the customer lifecycle."""

    date = models.DateTimeField(default=timezone.now, editable=False)
    type = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in CustomerEvents.CHOICES
        ],
    )
    # order = models.ForeignKey("order.Order", on_delete=models.SET_NULL, null=True)
    # auction = models.ForeignKey("order.Order", on_delete=models.SET_NULL, null=True)
    
    
    
    parameters = JSONField(blank=True, default=dict, encoder=CustomJsonEncoder)
    user = models.ForeignKey(
        DjolowinUser, related_name="events", on_delete=models.CASCADE, null=True
    )
    # app = models.ForeignKey(App, related_name="+", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ("date",)

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type!r}, user={self.user!r})"
    

class StaffNotificationRecipient(models.Model):
    user = models.OneToOneField(
        DjolowinUser,
        related_name="staff_notification",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    staff_email = models.EmailField(unique=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("staff_email",)

    def get_email(self):
        return self.user.email if self.user else self.staff_email