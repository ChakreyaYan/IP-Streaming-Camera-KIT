from django import forms
from .models import Camera

class CameraForm(forms.ModelForm):
	ip = forms.CharField(max_length=30, help_text= "Please enter the category name.")
	name = forms.CharField(max_length=100, help_text="Pleas enter the category name")
	# location = forms.CharField(max_length=100, help_text="Pleas enter the category name")
	# option  = forms.CharField(max_length=100 , help_text="Pleas Enter the value")
	class Meta:
		model = Camera
		fields = ('ip', 'name',)
