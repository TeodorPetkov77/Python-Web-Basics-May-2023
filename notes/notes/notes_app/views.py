from django.shortcuts import render, redirect

from notes.notes_app.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes.notes_app.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def add_profile(request):
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
        'form': form,
        'hide_nav': True,
    }

    return render(
        request,
        'home-no-profile.html',
        context
    )


def home_page(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    notes = Note.objects.all().order_by('-id')

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    form = NoteCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
        'hide_add_note': True
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "GET":
        form = NoteEditForm(instance=note, initial=note.__dict__)
    else:
        form = NoteEditForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect('home page')

    form = NoteDeleteForm(initial=note.__dict__)

    context = {
        'form': form
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = Profile.objects.get()
    notes_count = Note.objects.all().count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('home page')
