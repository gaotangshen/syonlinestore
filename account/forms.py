from django import forms
from django.contrib.auth.models import User
# from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"Username",
        error_messages={'required': 'Username'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"Username",
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label=u"Password",
        error_messages={'required': u'Password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"Password",
            }
        ),
    )   
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"Username and Password are required")
        else:
            cleaned_data = super(LoginForm, self).clean() 

class RegistrationForm(forms.Form):
 
    username = forms.RegexField(
        regex=r'^\w+$', 
        required=True,
        widget=forms.TextInput(attrs=dict( max_length=30)), 
        label="Username", 
        error_messages={ 'invalid': "This value must contain only letters, numbers and underscores." }
        )
    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
        label="Email address")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), 
        label="Password",)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), 
        label="Password (again)")
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data