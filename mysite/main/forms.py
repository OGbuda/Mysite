from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Download
from django.forms import ModelForm, TextInput, FileInput, Textarea, PasswordInput, CharField


class VideoForm(ModelForm):
    class Meta:
        model = Download
        fields = ["name","content","description"]

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название видео'
            }),


            "content": FileInput(attrs={
                'class': 'form-control-file',

            }),

            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание видео видео'
            })
        }




class RegisterUserForm(UserCreationForm):
    username = CharField(label='', widget=TextInput(attrs={'class': 'inputfield', 'placeholder': 'Логин'}))
    password1 = CharField(label='', widget=PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Пароль'}))
    password2 = CharField(label='', widget=PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'inputfield', 'placeholder': 'Логин'}),
            'password1': PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Придумайте пароль'}),
            'password2': PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Повторите пароль'}),
        }


class AuthenticationForm(UserCreationForm):
    username = CharField(label='', widget=TextInput(attrs={'class': 'inputfield', 'placeholder': 'Логин'}))
    password = CharField(label='', widget=PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'inputfield', 'placeholder': 'Логин'}),
            'password': PasswordInput(attrs={'class': 'inputfield', 'placeholder': 'Пароль'}),
        }