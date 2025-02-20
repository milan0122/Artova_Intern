from django import forms
from .models import Task,Profile
from django.contrib.auth.models import User 

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', 'password']

    def clean_password_confirm(self):
        password= self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password  != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','location','profile_picture']