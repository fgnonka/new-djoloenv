from django.shortcuts import render
from base.models.portfolio import Portfolio
from base.models.playercard import PlayerCard

def PortfolioPage(request):
    context = {
        'portfolios': Portfolio.objects.all()
    }
    return render(request, 'base/portfolio.html',context)