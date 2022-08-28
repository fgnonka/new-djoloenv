from base.models.player import Player
from base.models.playercard import PlayerCard
from base.models.team import Team
from base.models.rarity import Rarity
import unidecode


for i in Player.objects.all():
    shortname = unidecode.unidecode(i.name)
    print(shortname.lower().replace(' ', '-'))
    count = 1
    while count <= 10:
        card = PlayerCard.objects.create(player=i,
                rarity=Rarity.objects.get(id=1),index=int(count))
        # PlayerCard.objects.filter(id=card.id).update(slug=shortname.lower().replace(' ', '-') +'-'+ card.rarity.name.lower()+ '-' +str(count))
        count+=1