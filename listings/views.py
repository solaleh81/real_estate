from django.shortcuts import render
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', context={'listings': listings})

def listing_retrieve(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, 'listing.html', context={'listing': listing})

def listing_create(request):
    form = ListingForm()
    return render(request, 'listing_create.html', context={'form': form})