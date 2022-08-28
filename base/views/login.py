from django.shortcuts import render

def LoginPage(request):
    return render(request, 'base/login.html')