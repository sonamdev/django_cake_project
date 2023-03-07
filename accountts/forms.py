from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='* Required. Enter first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='* Required. Enter last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='* Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=10, required=True, help_text='* Required. Enter a 10-digit phone number.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone_number
#cyclometric complexity