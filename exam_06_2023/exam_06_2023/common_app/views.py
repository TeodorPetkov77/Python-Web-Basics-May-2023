from django.shortcuts import render

from exam_06_2023.fruit_app.models import Fruit
from exam_06_2023.profile_app.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index_page(request):
    context = {
        'profile': get_profile()
    }

    return render(request, 'index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all().order_by('-id')

    context = {
        'profile': get_profile(),
        'fruits': fruits,
    }

    return render(request, 'dashboard.html', context)
