from django.shortcuts import render
from .models import Post, Answer
from .forms import PostForm

import os

def post_list(request):
    posts = Post.objects.all()
    message = ''
    print(request.POST)
    data = request.POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        form = PostForm(data)
        if form.is_valid():
            try:
                # TODO: ここでformを正しくSaveする。
                print(form)
                result = {}
                for num, question in enumerate(posts):
                    print(num)
                    # make a result dict
                    if str(num+1) in data:
                        result[question.text] = convert_to_answer(data[str(num+1)])
                    else:
                        result[question.text] = None
                    print(num)
                ans = Answer()
                ans.answer = result
                ans.save()
                message = "保存しました"
            except (KeyError, Post.DoesNotExist):
                return render(request, 'question/post_list.html', {
                    'posts': posts,
                    'message': "投票内容を選んでください",
                })
    return render(request, 'question/post_list.html', {'posts': posts, 'message': message})

def convert_to_answer(answer_num):
    choices = {'1': '満足',
               '2': 'やや満足',
               '3': 'どちらとも言えない',
               '4': 'やや不満',
               '5': '不満'}
    return choices[answer_num]
