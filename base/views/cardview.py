from django.shortcuts import render
from django.views.generic import DetailView, ListView
from base.models.playercard import PlayerCard

allplayers = PlayerCard.objects.all()


class CardDetailView(DetailView):
    model = PlayerCard
    template_name = 'base/playercard.html'
# def CardView(request, slug):
#     playercard = None
#     for i in allplayers:
#         if (i.slug) == str(slug):
#             playercard = i
#             cardfilter = len(PlayerCard.objects.filter(player=playercard.player))
#     context = {'playercard': playercard, 'cardfilter': cardfilter}
#     return render(request, 'base/playercard.html', context)