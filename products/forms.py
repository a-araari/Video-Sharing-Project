from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
	title = forms.CharField(max_length=255,
		widget=forms.TextInput(attrs={'class':'form-control adem-input'}))
	description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control adem-input'}))
	tuto_url = forms.CharField(max_length=255,
		widget=forms.TextInput(attrs={'class':'form-control adem-input', 'placeholder': 'e.g : https://www.youtube.com/watch?v='}))

	class Meta():
		model = Product
		fields = [
			'title',
			'description',
			'tuto_url'
		]
	
	def clean_tuto_url(self):
		print('called')
		url = self.cleaned_data['tuto_url']
		n_url = ''
		if '?v=' in url:
			n_url = 'https://www.youtube.com/embed/' + url.split('?v=')[-1]
		else:
			n_url = 'https://www.youtube.com/embed/' + url
		return n_url
#https://www.youtube.com/embed/