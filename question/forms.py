
from django import forms
from .models import Answer

CHOICES = [('1', '満足'),
           ('2', 'やや満足'),
           ('3', 'どちらとも言えない'),
           ('4', 'やや不満'),
           ('5', '不満')]


class PostForm(forms.Form):
    '''
    postform = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
    )
    '''

    class Meta:
        model = Answer
        withgets = {
            'answer': forms.RadioSelect()
        }