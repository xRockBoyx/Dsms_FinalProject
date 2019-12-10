from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    deparement = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20)
    password = forms.CharField(required=True)
