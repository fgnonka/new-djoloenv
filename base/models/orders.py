from django.db import models
from .playercard import PlayerCard
from .bundle import Bundle
from base.models.djolouser import DjolowinUser


class CardOrder(models.Model):
    PlayerCard = models.ForeignKey(PlayerCard, on_delete=models.CASCADE)
    customer = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return CardOrder.objects.filter(customer=customer_id).order_by('-date')
        
class BundleOrder(models.Model):
    Bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    customer = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return BundleOrder.objects.filter(customer=customer_id).order_by('-date')