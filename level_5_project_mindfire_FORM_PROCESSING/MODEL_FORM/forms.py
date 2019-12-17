from django import forms
from MODEL_FORM.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
