from django import forms
from django.core import validators
# widgets = field to html input

class contactForm(forms.Form):
    name = forms.CharField(label = "User Name: ", help_text = "Enter Your Full Name", required=False, widget = forms.Textarea(attrs = {'id': 'text_area', 'class' : 'class1 class2', 'placeholder': 'Enter your name'}))

    # file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget = forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs ={'type':'date'}))

    appointment = forms.CharField(widget=forms.DateInput(attrs ={'type':'datetime-local'}))

    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]

    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    meal = [('Pepperoni', 'Pepperoni'), ('Mashroom', 'Mashroom'), ('Beef', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname)<10:
#     #         raise forms.ValidationError('Enter a name with atleast 10 char')
#     #     else:
#     #         return valname 
        
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     else:
#     #         return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname)<10:
#             raise forms.ValidationError('Enter a name with atleast 10 char')
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")



class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with atleast 10 char')])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])

    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),
                    validators.MinValueValidator(24, message="age must be at least 24")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='File extension not allowed we need pdf')])


class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        if (val_con_pass != val_pass):
            raise forms.ValidationError("Password not matched")

