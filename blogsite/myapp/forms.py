from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Blogsite
from django.core.exceptions import ValidationError  
from django import forms

class NewUserForm (UserCreationForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'focus_outline-none'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput (attrs={'class':'focus_outline-none','placeholder':'e.g. email@address.com'}))
    password1=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus_outline-none'}))
    password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus_outline-none'}))

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  

    def save(self, commit = True):  
        user = User.objects.create_user(  
        self.cleaned_data['username'],  
        self.cleaned_data['email'],  
        self.cleaned_data['password1']  
        )  
        return user  


class RegisteredUserForm(UserCreationForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'focus_outline-none'}) )
    password=forms.CharField(required=True,widget=forms.PasswordInput (attrs={'class':'focus_outline-none'}))

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blogsite
        fields = ['title', 'content', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class':'title1','placeholder':'enter your title'}),
            'content': forms.Textarea(attrs={'class':'content1', 'placeholder':'enter your content'}),
        }
  
