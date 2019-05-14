from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = PostForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        try:
            # TODO: ここでformを正しくSaveする。
            print(form)
        except (KeyError, Post.DoesNotExist):
            return render(request, 'question/post_list.html', {
                'posts': posts,
                'message': "投票内容を選んでください",
            })
    return render(request, 'question/post_list.html', {'posts': posts})