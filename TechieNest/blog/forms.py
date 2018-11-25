from django import forms
from .models import Comment,Post
from django.core.exceptions import ValidationError

class CommentsForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
    }))
    comment_text=forms.CharField(widget=forms.TextInput(attrs={
        'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    class Meta:
        model=Comment
        fields=['text','author','email','website']
