from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserloginForm(forms.Form):
    """Form for user to input login details"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """Frorm is used to register the user"""
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget = forms.PasswordInput)

    class Meta: # Inner class is used by Djano to provide infomation about the forms.
        model = User # Specifies the name of the model where we want to store user information
        fields = ['email', 'username', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if not password1 or not password2:
            raise ValidationError("Please confirm your passwword")
    
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2
    
    
    
    