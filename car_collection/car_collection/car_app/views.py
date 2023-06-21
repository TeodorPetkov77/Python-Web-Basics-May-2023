from profile import Profile

from car_collection.car_app.forms import CreateCarForm, EditCarForm, DeleteCarForm
from car_collection.car_app.models import Car
from car_collection.profile_app.models import Profile
from django.shortcuts import render, redirect


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def car_create(request):
    profile = get_profile()
    form = CreateCarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-create.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    context = {
        'profile': profile,
        'car': car
    }
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    if request.method == "GET":
        form = EditCarForm(instance=car, initial=car.__dict__)
    else:
        form = EditCarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    if request.method == "POST":
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(initial=car.__dict__)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-delete.html', context)
