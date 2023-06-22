from django.shortcuts import render, redirect

from gamesplay.common_app.views import get_profile
from gamesplay.game_app.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay.game_app.models import Game


def create_game(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    form = CreateGameForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    game = Game.objects.get(pk=pk)

    context = {
        'profile': profile,
        'game': game
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    game = Game.objects.get(pk=pk)

    if request.method == "GET":
        form = EditGameForm(instance=game, initial=game.__dict__)
    else:
        form = EditGameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    game = Game.objects.get(pk=pk)

    if request.method == "POST":
        game.delete()
        return redirect('dashboard')

    form = DeleteGameForm(initial=game.__dict__)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-game.html', context)
