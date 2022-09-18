from django.contrib import admin

from .djolouser import (DjolowinUser, CustomerEvent, StaffNotificationRecipient)
# Register your models here.
admin.site.register(DjolowinUser)
admin.site.register(CustomerEvent)
admin.site.register(StaffNotificationRecipient)
