from django.shortcuts import render

from car_collection.car_app.models import Car
from car_collection.profile_app.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'catalogue.html', context)
