from django import forms
from UserAPP.models import User

class UserForm(forms.ModelForm):
      class Meta:
          model=User
          fields = "__all__"