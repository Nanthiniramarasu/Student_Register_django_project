from django import forms
from Myapplication.models import Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# ---------------------------
# CRUD Form for Data Model
# ---------------------------
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'contact', 'address', 'mail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

# ---------------------------
# Signup Form (User Creation)
# ---------------------------
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# ---------------------------
# Login Form
# ---------------------------
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter password'
    }))
