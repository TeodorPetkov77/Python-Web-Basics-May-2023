from django import forms

from car_collection.car_app.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'type',
            'model',
            'year',
            'image_url',
            'price',
        ]

        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
