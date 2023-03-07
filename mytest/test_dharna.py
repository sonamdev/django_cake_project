from django.test import TestCase
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User


class RegistrationFormTestCase(TestCase):
    def test_form_fields(self):
        form_data= {'First':'joey','last_name':'django','username':'joeyd','email':'joey@gmail.com','phone_number':'1234567892',
                    'password1':'pass@1234', 'password2':'pass'}
        form= RegistrationForm(data=form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field.label, error)
        
        self.assertTrue(form.is_valid())

        self.assertEqual('expected output', 'actual output')
      
    def test_invalid_email(self):
        form_data= {'first_name':'joey','last_name':'django','username':'joeyd','email':'joeygmail.com','phone_number':'1234567892',
                    'password1':'pass@1234', 'password2':'pass@1234'}
        form= RegistrationForm(data=form_data)
        
        self.assertFalse(form.is_valid())


#debugger.




