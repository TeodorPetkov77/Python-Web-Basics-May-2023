from django.shortcuts import render, redirect

from car_collection.car_app.models import Car
from car_collection.profile_app.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from car_collection.profile_app.models import Profile


def total_cars_price_sum():
    cars = Car.objects.all()
    total_price = 0
    for car in cars:
        total_price += car.price

    return total_price


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def profile_create(request):
    if get_profile() is not None:
        return redirect('index page')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    profile_first_name = profile.first_name
    profile_last_name = profile.last_name
    total_cars_price = total_cars_price_sum()

    context = {
        'profile': profile,
        'profile_first_name': profile_first_name,
        'profile_last_name': profile_last_name,
        'total_cars_price': total_cars_price,
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileEditForm(instance=profile, initial=profile.__dict__)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    cars = Car.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            cars.delete()
            return redirect('index page')

    context = {
        'form': form
    }

    return render(request, 'profile-delete.html', context)
