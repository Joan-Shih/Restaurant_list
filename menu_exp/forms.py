from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)

class  RegisterForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)
	email = forms.EmailField()
	
	
