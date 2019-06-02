from django.shortcuts import render
from .models import Post, Answer
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    user = request.user
    message = ''

    data = request.POST
    if request.method == 'POST':
        form = PostForm(data)
        if form.is_valid():
            try:
                result = {}
                for num, question in enumerate(posts):
                    # make a result dict
                    if question.text in data:
                        result[question.text] = eval("question." + data[question.text])
                    else:
                        result[question.text] = None
                ans = Answer(
                    user=data['csrfmiddlewaretoken'],
                    question=list(result.keys()),
                    answer=list(result.values())
                )
                ans.save()
                message = "保存しました"
            except (KeyError, Post.DoesNotExist):
                return render(request, 'question/post_list.html', {
                    'posts': posts,
                    'message': "投票内容を選んでください",
                })
    return render(request, 'question/post_list.html', {'posts': posts, 'message': message})

