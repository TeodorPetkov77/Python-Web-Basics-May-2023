from django import forms

from recipes.recipes_app.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(),
        #     'image_url': forms.URLField(),
        #     'description': forms.TextInput(),
        #     'ingredients': forms.TextInput(),
        #     'time': forms.IntegerField(),
        # }
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time (Minutes)'
        }


class RecipeForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
