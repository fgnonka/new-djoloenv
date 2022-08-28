from django.urls import path, include
from .views.home import HomeView, CardView
from .views.register import RegisterPage
from .views.login import LoginPage
from django.contrib.auth.views import LogoutView



urlpatterns = [    
    path('login/', LoginPage, name='login'),
    path('playercard/<str:slug>/', CardView, name='playercard'),
    path('register/', RegisterPage, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView, name='home'),
    
]
