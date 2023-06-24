from django.shortcuts import render, redirect

from exam_06_2023.common_app.views import get_profile
from exam_06_2023.fruit_app.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from exam_06_2023.fruit_app.models import Fruit


def create_fruit(request):
    form = FruitCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):

    fruit = Fruit.objects.get(pk=pk)
    context = {
        'profile': get_profile(),
        'fruit': fruit,
    }

    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):

    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = FruitEditForm(instance=fruit, initial=fruit.__dict__)
    else:
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):

    fruit = Fruit.objects.get(pk=pk)

    if request.method == "POST":
        fruit.delete()
        return redirect('dashboard')

    form = FruitDeleteForm(initial=fruit.__dict__)

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'delete-fruit.html', context)