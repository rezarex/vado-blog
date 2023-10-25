from django import forms
from .models import Blog
from markdownx.fields import MarkdownxFormField
#from martor.fields import MartorFormField

class BlogForm(forms.ModelForm):
    body = MarkdownxFormField() #MartorFormField()

    class Meta:
        model = Blog
        fields = ['title', 'is_active']