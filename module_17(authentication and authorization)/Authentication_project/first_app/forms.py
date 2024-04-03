from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, UserChangeForm
from django import forms

class ReginsterForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'id':'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = ''


class setPass(SetPasswordForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field_name in self.fields:
            self.fields[field_name].help_text = ''


class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]