from django import forms

from .models import Contabilidad

class PostForm(forms.ModelForm):

    class Meta:
            model = Contabilidad
            fields = ('text', 'text',)