from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    form = PostForm(request.POST or None)
    message = ''
    if request.method == "POST":
        print(request.POST)
        try:
            # TODO: ここでformを正しくSaveする。
            print(form)
            message = "保存しました"
        except (KeyError, Post.DoesNotExist):
            return render(request, 'question/post_list.html', {
                'posts': posts,
                'message': "投票内容を選んでください",
            })
    return render(request, 'question/post_list.html', {'posts': posts, 'message': message})
