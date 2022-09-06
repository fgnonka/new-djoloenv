from django.shortcuts import render
from .models import Bundle
# Create your views here.

def bundle_list(request):
    context = {
        'bundles': Bundle.objects.all()
    }
    return render(request, "trades/bundle_list.html", context)