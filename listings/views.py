from django.shortcuts import render
from .models import Listing

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', context={'listings': listings})


