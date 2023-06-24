from django.shortcuts import render, redirect

from exam_06_2023.common_app.views import get_profile
from exam_06_2023.fruit_app.models import Fruit
from exam_06_2023.profile_app.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


def create_profile(request):

    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):

    profile = get_profile()

    if not profile:
        return redirect('create profile')

    fruits_count = Fruit.objects.all().count()
    context = {
        'profile': profile,
        'fruits_count': fruits_count,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

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

    if not profile:
        return redirect('create profile')

    fruits = Fruit.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            fruits.delete()
            return redirect('index page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)