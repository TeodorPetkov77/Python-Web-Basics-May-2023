from django.shortcuts import render, redirect

from recipes.recipes_app.forms import RecipeForm, RecipeDeleteForm
from recipes.recipes_app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        recipe.delete()
        return redirect('index')

    form = RecipeDeleteForm(initial=recipe.__dict__)
    context = {
        'form': form
    }

    return render(request, 'delete.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe, initial=recipe.__dict__)

    else:
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'edit.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    photo = recipe.image_url
    ingredients = [ingred.strip() for ingred in recipe.ingredients.split(",")]
    description = recipe.description

    context = {
        'recipe': recipe,
        'photo': photo,
        'ingredients': ingredients,
        'description': description,
    }

    return render(request, 'details.html', context)
