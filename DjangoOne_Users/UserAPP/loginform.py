from django import forms
from django.contrib.auth.models import User as adminuser
from UserAPP.models import UserProfileInfo

class UserForm(forms.ModelForm):
      password = forms.CharField(widget=forms.PasswordInput())

      class Meta:
          model=adminuser
          fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
     class Meta:
         model=UserProfileInfo
         fields = ('portfolio_site','profile_pic')
