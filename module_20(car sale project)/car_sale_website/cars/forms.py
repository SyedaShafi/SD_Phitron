from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import CommentModel

class RegintrationForm(UserCreationForm):
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



class CommentForm(forms.ModelForm):
    class Meta: 
        model = CommentModel
        fields = ['name', 'email', 'body']