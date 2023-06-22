from django import forms

from gamesplay.game_app.models import Game


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'category',
            'rating',
            'max_level',
            'image_url',
            'summary'
        ]

        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary'
        }


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
