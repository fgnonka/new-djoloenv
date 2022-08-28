from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AuctionList, Bid, AuctionWinner 
# Create your views here.


class AuctionListView(ListView):
    model = AuctionList
    template_name = 'auctions/auction-main.html'
    
class AuctionDetailView(DetailView):
    model = AuctionList
    template_name = 'auctions/countdown.html'