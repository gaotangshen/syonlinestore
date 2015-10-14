from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label="Your Name", max_length=100)

