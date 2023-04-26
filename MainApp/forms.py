from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.contrib.auth.models import User


class AddNotebookForm(forms.ModelForm):

    class Meta:
        model = Notebook
        disp = forms.ModelChoiceField(queryset=Display.objects.all())
        disp_type = forms.ModelChoiceField(queryset=DisplayType.objects.all())
        proc = forms.ModelChoiceField(queryset=Processor.objects.all())
        gc = forms.ModelChoiceField(queryset=GraphicsCard.objects.all())
        r_a_m = forms.ModelChoiceField(queryset=RAM.objects.all())
        hd = forms.ModelChoiceField(queryset=HardDisk.objects.all())
        o_s = forms.ModelChoiceField(queryset=OS.objects.all())
        fields = ['disp', 'disp_type', 'proc', 'gc', 'r_a_m', 'hd', 'o_s']
        widgets = {
            'disp': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'disp_type': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'proc': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'gc': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'r_a_m': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'hd': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
            'o_s': forms.Select(
                attrs={'class': 'btn btn-success dropdown-toggle', 'type': 'button', 'data-bs-toggle': 'dropdown',
                       'aria-expanded': 'false'}),
        }

class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise forms.ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))