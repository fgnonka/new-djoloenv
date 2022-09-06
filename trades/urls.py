from django.urls import path, include
from .views import bundle_list

app_name = 'trades'

urlpatterns = [
    path('', bundle_list, name = 'bundle-list'),
]
