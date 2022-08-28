from django.urls import path
from .views import AuctionDetailView, AuctionListView

app_name = 'auctions'

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction-list'),
    path('<pk>/', AuctionDetailView.as_view(), name='auction-detail')
    
]