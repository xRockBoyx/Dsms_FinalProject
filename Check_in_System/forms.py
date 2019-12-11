from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    deparement = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    #stu_id = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ("deparement", "name","phone","email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.deparement = self.cleaned_data["deparement"]
        user.name = self.cleaned_data["name"]
        user.phone = self.cleaned_data["phone"]
       # user.stu_id = self.cleaned_data["stu_id"]
        if commit:
            user.save()
        return user
    
    
    
