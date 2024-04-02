from django import forms
import datetime


class contactForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # comment = forms.CharField(widget=forms.Textarea)
    # comment = forms.CharField(widget=forms.Textarea(attrs = {'rows':3}))
    # agree = forms.BooleanField()
    # BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    # birth_year = forms.DateField(widget= forms.SelectDateWidget( ))
    # date = forms.DateField(widget=NumberInput(attrs = {'type':'date'}))
    # value = forms.DateField(required = False)
    # message = forms.CharField(max_length = 10, required = False)
    # email_address = forms.EmailField(label = "Please enter your email address")

    # first_name = forms.CharField(initial = "Your name")
    # agree = forms.BooleanField(initial=False)
    # day = forms.DateField(initial = datetime.date.today)
    fav_clr = [
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices = fav_clr)
    favorite_color_radio = forms.ChoiceField(widget=forms.RadioSelect, choices = fav_clr)
    favorite_color_multiple_choice = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices=fav_clr)
   
