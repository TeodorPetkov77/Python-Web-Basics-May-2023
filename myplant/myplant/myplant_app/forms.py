from django import forms

from myplant.myplant_app.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'profile_picture',

        ]

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
        ]

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Profile.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'plant_type',
            'name',
            'image_url',
            'description',
            'price',
        ]

        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image_url': 'Image Url',
            'description': 'Description',
            'price': 'Price',
        }


class PlantCreateForm(BasePlantForm):
    pass


class PlantEditForm(BasePlantForm):
    pass


class PlantDeleteForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
