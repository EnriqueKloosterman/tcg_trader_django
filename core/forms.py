from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Password'
    }))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Email'
    })) 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Confirm Password'
    }))
