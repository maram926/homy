from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'form-control py-2'
    }))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'form-control'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'form-control',
        'autocomplete': ''
    }))  

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email',
        'class':'form-control'
    })) 

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'form-control'
    })) 

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'entier your password agin',
        'class':'form-control'
    }))   
