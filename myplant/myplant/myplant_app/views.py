from django.shortcuts import render, redirect

from myplant.myplant_app.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileDeleteForm, ProfileEditForm
from myplant.myplant_app.models import Plant, Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'home-page.html', context)


def show_catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'plants': plants,
        'profile': profile,
    }

    return render(request, 'catalogue.html', context)


def create_plant(request):
    profile = get_profile()
    form = PlantCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('show catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def details_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.get(pk=pk)

    context = {
        'profile': profile,
        'plant': plant,
    }

    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.get(pk=pk)

    if request.method == "GET":
        form = PlantEditForm(instance=plant, initial=plant.__dict__)
    else:
        form = PlantEditForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.get(pk=pk)

    if request.method == "POST":
        plant.delete()
        return redirect('home page')

    form = PlantDeleteForm(initial=plant.__dict__)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-plant.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('home page')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    plants_count = Plant.objects.all().count()

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileEditForm(instance=profile, initial=profile.__dict__)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            plants.delete()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
