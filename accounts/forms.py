from  django.contrib.auth import get_user_model
from django.forms import forms

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')