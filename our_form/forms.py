from django import forms
from .models import information

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(required=False)

class SignupForm(forms.ModelForm):
	class Meta:
		model = information
		fields = ['name','address','phone']

	def clean_name_text(self):
		name_text = self.cleaned_data.get('name')
		return name_text
