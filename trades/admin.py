from django.contrib import admin
from .models import (Bundle, BundleOrder, SingleCard, OwnedCard, SingleOrder, SingleOrderCard)

# Register your models here.

class SingleOrderAdmin(admin.ModelAdmin):
    list_display = ['buyer',
                    'card',
                    'is_sold',
                    'sold_date'
                    ]
    list_display_links = [
        'buyer',
        'card'
    ]
    list_filter = ['buyer',
                   'card',
                   'sold_date'
                    ]
    search_fields = [
        'buyer__username',
    ]

class BundleOrderAdmin(admin.ModelAdmin):
    list_display = ['buyer',
                    'bundle',
                    'is_sold',
                    'sold_date'
                    ]
    list_display_links = [
        'buyer',
        'bundle'
    ]
    list_filter = ['buyer',
                   'bundle',
                   'sold_date'
                    ]
    search_fields = [
        'buyer__username',
    ]

admin.site.register(BundleOrder, BundleOrderAdmin)
admin.site.register(Bundle)
admin.site.register(SingleCard)
admin.site.register(OwnedCard)
admin.site.register(SingleOrder, SingleOrderAdmin)
admin.site.register(SingleOrderCard)
