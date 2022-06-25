from django import  forms
from .models import *


class Create(forms.ModelForm):
    class Meta:
        fields = ['url', 'pic_url', 'title', 'description' ]
        model = item

        widgets = {
            'url': forms.TextInput(attrs={'class':"input is-large", "style":'width: 300px; margin-bottom:10px', 'placeholder':'source'}),
            'pic_url': forms.TextInput(attrs={'class':"input is-large", "style":'width: 300px; margin-bottom:10px', 'placeholder':'picture'}),
            'title': forms.TextInput(attrs={'class':"input is-large", "style":'width: 300px; margin-bottom:10px', 'placeholder':'title'}),
            'description': forms.Textarea(attrs={'class':"textarea", 'rows':
            '3',"style":'width: 300px; margin-bottom:10px', 'placeholder':'description'}),
        }

        labels = {
            'url':'',
            'pic_url':'',
            'title':'',
            'description':
            '',
        }