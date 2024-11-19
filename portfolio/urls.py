from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page
    path('entries/', views.portfolio_list, name='portfolio_list'),  # Entries Page
]
