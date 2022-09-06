from django.urls import path, include
from .views.portfolio import PortfolioPage
from .views.home import HomeView
from .views.cardview import CardDetailView
from .views.register import RegisterPage
from .views.login import LoginPage
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [    
    path('login/', LoginPage, name='login'),
    path('playercard/<str:slug>/', CardDetailView.as_view(), name='playercard'),
    path('register/', RegisterPage, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('portfolio/', PortfolioPage, name='portfolio'),
    path('', HomeView, name='home'),
    
]
