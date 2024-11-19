from django.shortcuts import render
from .models import PortfolioEntry

# Create your views here.

def portfolio_list(request):
    entries = PortfolioEntry.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'entries': entries})

def home(request):
    return render(request, 'portfolio/home.html')