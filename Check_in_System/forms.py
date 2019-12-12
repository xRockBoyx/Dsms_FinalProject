from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    deparement = forms.CharField(
        max_length=20,
        widget=forms.Select(
            choices=[('1','IECS'),('2','RCE'),('3','DCL'),('4','DEE')],
            attrs={
                'class':'form-control'
            }
        )
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder':'姓名',
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email address',
                'class':'form-control'
            }
        )
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Phone number'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Create password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Repeat password'
            }
        )
    )
    # name = forms.TextInput(
    #     max_length=100,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder':'姓名',
    #             'class':'form-control'
    #         }
    #     )
    # )
    #name = forms.CharField(max_length=100)
    
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
    
    
    
