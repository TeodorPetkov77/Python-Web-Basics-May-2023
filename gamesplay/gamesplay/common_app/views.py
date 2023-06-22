from django.shortcuts import render

from gamesplay.game_app.models import Game
from gamesplay.profile_app.models import Profile


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


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all().order_by('-id')

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'dashboard.html', context)
