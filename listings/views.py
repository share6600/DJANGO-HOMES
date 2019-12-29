from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Listing
from django.shortcuts import get_object_or_404
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # creat paginator
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listings': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
