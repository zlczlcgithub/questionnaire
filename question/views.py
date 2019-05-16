from django.shortcuts import render
from .models import Post
from .forms import PostForm

import os

def post_list(request):
    posts = Post.objects.all()
    message = ''
    print(request.POST)
    data = request.POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form.is_valid())
        form = PostForm(data)
        if form.is_valid():
            try:
                # TODO: ここでformを正しくSaveする。
                print(form)
                # form.save(commit=False)
                message = "保存しました"
            except (KeyError, Post.DoesNotExist):
                return render(request, 'question/post_list.html', {
                    'posts': posts,
                    'message': "投票内容を選んでください",
                })
            # try:
            # TODO: ここでformを正しくSaveする。
            save_dict_to_file(data, os.getcwd() + "/question/history_data/" + data["csrfmiddlewaretoken"] + ".txt")
            message = "保存しました"
            # except (KeyError, Post.DoesNotExist):
            #     return render(request, 'question/post_list.html', {
            #         'posts': posts,
            #         'message': "投票内容を選んでください",
            #     })
    return render(request, 'question/post_list.html', {'posts': posts, 'message': message})

def save_dict_to_file(dic, filename):
  f = open(filename,'w')
  f.write(str(dic))
  f.close()