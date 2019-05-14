from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    postform = forms.ModelChoiceField(
        queryset=Post.objects.all(),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Post
        fields = '__all__'


