from django.shortcuts import render
from .models import PortfolioEntry
from django.conf import settings

# Create your views here.

def portfolio_list(request):
    entries = PortfolioEntry.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {
        'entries': entries,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def home(request):
    return render(request, 'portfolio/home.html')