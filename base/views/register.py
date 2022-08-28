from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def RegisterPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            form= UserCreationForm()
            
    context = {'form': form}
    return render(request, 'base/register.html', context)