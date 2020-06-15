from django import forms
from . import models

class CreateMovie(forms.ModelForm):
	class Meta:
		model = models.Movie
		fields = ['title','slug','body','thumb','videofile']
		
 