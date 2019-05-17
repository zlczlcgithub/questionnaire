
from django import forms
from .models import Answer

class PostForm(forms.Form):
    class Meta:
        model = Answer
        withgets = {
            'answer': forms.RadioSelect()
        }