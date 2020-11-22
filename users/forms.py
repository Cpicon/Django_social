"""User forms"""

from django import forms
from django.contrib.auth.models import User

# Models
from users.models import Profile


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.EmailField(min_length=6, max_length=50, widget=forms.EmailInput())

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username already in use.')
        return username

    def clean_email(self):
        """Email must be unique"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email already exists')
        return email

    def clean(self):
        """Validation password and password confirmation matching"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError(' Passwords do not macth')
        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForms(forms.Form):
    website = forms.URLField(max_length=200)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField()
