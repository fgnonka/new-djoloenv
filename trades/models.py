from django.db import models
from django.urls import reverse
from user_account.djolouser import DjolowinUser
from base.models.playercard import PlayerCard
from django_prices.models import MoneyField
# Create your models here.


class OwnedCard(models.Model):
    # This model represents the cards that are owned by a DjolowinUser
    owner = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE)
    card = models.ForeignKey(PlayerCard, on_delete=models.CASCADE)
    price = MoneyField(
        amount_field="card_price", currency_field="DJOL"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['card']
    
    def __str__(self) -> str:
        return f"Card: {self.card}"
    
class SingleCard(models.Model):
# This model represent the cards that will be issued by the Djolowin platform at a premium price
    card = models.ForeignKey(PlayerCard, on_delete=models.CASCADE)
    price = MoneyField(
        amount_field="card_price", currency_field="DJOL"
    ) 

    
class SingleOrderCard(models.Model):
    # This model is an in-between card model for when a user submit a request to buy a SingleCard
    tradecard = models.ForeignKey(SingleCard, on_delete=models.CASCADE)
    class Meta:
        ordering = ['tradecard']
    
    def __str__(self) -> str:
        return f"Card: {self.tradecard}"
    
class SingleOrder(models.Model):
    # This model contains information about a SingleCard order
    buyer = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE, related_name='single_buyer')
    card = models.ForeignKey(SingleOrderCard, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    sold_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"Order# {self.id}, bought by: {self.buyer}"
    
    @staticmethod
    def get_single_orders_by_customer(customer_id):
        return SingleOrder.objects.filter(customer=customer_id).order_by('-sold_date')
    
    
class Bundle(models.Model):
    # This model is an aggregation of Singlecards that are exclusively sold by Djolowin
    name = models.CharField(max_length=255)
    cards = models.ManyToManyField(
        PlayerCard, blank=True, related_name='bundle_cards')
    price = MoneyField(
        amount_field="bundle_price", currency_field="DJOL"
    )
    for_sale = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['pk']
    
    def __str__(self) -> str:
        return self.name + '-- Bundle ID#' + str(self.id)
    @staticmethod
    def get_active_bundle_list(active):
        return Bundle.objects.filter(for_sale=active).order_by('-created_date')
    
    
class BundleOrder(models.Model):
    buyer = models.ForeignKey(DjolowinUser, on_delete=models.CASCADE, related_name='bundle_buyer')
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    sold_date = models.DateTimeField()
    class Meta:
        ordering = ['bundle']
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return BundleOrder.objects.filter(buyer=customer_id).order_by('-sold_date')
    
    