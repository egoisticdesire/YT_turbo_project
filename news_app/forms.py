import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

from news_app.models import Category, News


class ContactForm(forms.Form):
    from_ = forms.CharField(
        label='От кого:',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    subject = forms.CharField(
        label='Тема письма:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    content = forms.CharField(
        label='Текст письма:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 20,
            },
        ),
    )

    captcha = CaptchaField(
        label='',
        widget=CaptchaTextInput(
            attrs={
                'class': 'form-control w-25 mt-4 d-inline-flex ms-2',
            },
        ),
    )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    password = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    password1 = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
            },
        ),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    email = forms.EmailField(
        label='E-mail:',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'content',
            'category',
            'is_published',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 20,
                },
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select text-bg-dark',
                },
            ),
            'is_published': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                },
            ),
        }
