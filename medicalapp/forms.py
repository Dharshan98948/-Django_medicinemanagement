from django import forms
from medicalapp.models import login,Medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class loginform(UserCreationForm):
    class Meta:
        model=login
        fields=['username','password']



class medicineform(forms.ModelForm):
    class Meta:
        model=Medicine
        fields='__all__'