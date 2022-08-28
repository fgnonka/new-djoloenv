from django.shortcuts import render
from base.models.playercard import PlayerCard
from base.models.player import Player
from base.models.bundle import Bundle
# Create your views here.

allplayers = PlayerCard.objects.all()
playercards = PlayerCard.objects.order_by('?')[:8]


def HomeView(request):
    context = {'playercards': playercards}
    return render(request, 'base/home.html', context)

def CardView(request, slug):
    playercard = None
    for i in allplayers:
        if (i.slug) == str(slug):
            playercard = i
            cardfilter = len(PlayerCard.objects.filter(player=playercard.player))
    context = {'playercard': playercard, 'cardfilter': cardfilter}
    return render(request, 'base/playercard.html', context)