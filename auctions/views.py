from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AuctionedCard, Bid, AuctionWinner 
# Create your views here.


class AuctionListView(ListView):
    model = AuctionedCard
    template_name = 'auctions/auction-main.html'
    
class AuctionDetailView(DetailView):
    model = AuctionedCard
    template_name = 'auctions/countdown.html'