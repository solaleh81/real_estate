from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', context={'listings': listings})

def listing_retrieve(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, 'listing.html', context={'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing is created successfully.")
            return redirect('list')
    else:
        form = ListingForm()

    return render(request, 'listing_create.html', context={'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(pk=id)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, id):
    listing = Listing.objects.get(pk=id)
    listing.delete()
    return redirect('list')