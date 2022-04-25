from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mycompany.models import UserProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    referral_email = forms.CharField(required=True)
    

    class Meta():
        model = UserProfileInfo
        fields = ( 'referral_email', 'bio')
