from django.shortcuts import render
from base.models.playercard import PlayerCard
from base.models.player import Player
# Create your views here.

allplayers = PlayerCard.objects.all()
playercards = PlayerCard.objects.order_by('?')[:6]


def HomeView(request):
    context = {'playercards': playercards}
    return render(request, 'base/home.html', context)

