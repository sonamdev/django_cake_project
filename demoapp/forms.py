from django import forms
class RegisterData(forms.Form):
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    email=forms.EmailField()
    

