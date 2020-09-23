from django import forms
from .models import Profile, Project, Participants, Soundtrack
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name',
                  'penname', 'email', 'password1', 'password2',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'penname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class ProjectUpdate(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description', 'genre', 'is_public']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'penname', 'email', 'avatar')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'penname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }


class AddingSoundtrack(forms.ModelForm):

    class Meta:
        model = Soundtrack
        fields = ('name', 'instrument', 'author', 'soundtrack', 'project')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'instrument': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.HiddenInput(attrs={'class': 'form-control'}),
            'soundtrack': forms.FileInput(attrs={'class': 'form-control'}),
            'project':forms.HiddenInput(attrs={'class': 'form-control'})
        }

class EditSoundtrack(forms.ModelForm):

    class Meta:
        model = Soundtrack
        fields = ('name', 'instrument')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'instrument': forms.Select(attrs={'class': 'form-control'}),
        }

# class savelyrics(forms.ModelForm):

#     class Meta:
#         model = Project
#         fields = ('lyrics')

#         fields = {
#             'lyrics': forms.TextInput(attrs={'class': 'form-control'})
#         }

class MyNewForm(forms.ModelForm):

    class Meta: 
        model = SuperAdmin
        fields = ('name','surname','position')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
        }
