from django.shortcuts import render, redirect

from gamesplay.common_app.views import get_profile
from gamesplay.game_app.models import Game
from gamesplay.profile_app.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


def calculate_average_rating():
    games = Game.objects.all()
    games_count = games.count()
    sum_rating = 0

    if not games:
        return 0.0

    for game in games:
        sum_rating += game.rating

    return sum_rating / games_count


def create_profile(request):
    profile = get_profile()
    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    average_rating = calculate_average_rating()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'average_rating': average_rating,
        'games': games
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

    games = Game.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            games.delete()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
