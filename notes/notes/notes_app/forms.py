from django import forms

from notes.notes_app.models import Profile, Note


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'age',
            'image_url',
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'content',
            'image_url',
        ]

        labels = {
            'title': 'Title',
            'content': 'Content ',
            'image_url': 'Link to Image',
        }


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
