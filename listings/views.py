from django.shortcuts import render
from .models import Listing

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', context={'listings': listings})

def listing_retrieve(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, 'listing.html', context={'listing': listing})
