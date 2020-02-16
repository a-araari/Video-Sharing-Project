from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

	username = forms.CharField(max_length=100,
			widget=forms.TextInput(attrs={'class':'form-control adem-input',
								'placeholder':'Username*'}))
	email = forms.EmailField(max_length=100, 
			widget=forms.TextInput(attrs={'class':'form-control adem-input',
								'placeholder':'Email'}), required=False)
	password1 = forms.CharField(max_length=100, 
			widget=forms.PasswordInput(attrs={'class':'form-control adem-input',
								'placeholder':'Password*'}))
	password2 = forms.CharField(max_length=100, 
			widget=forms.PasswordInput(attrs={'class':'form-control adem-input',
								'placeholder':'Confirm*'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']