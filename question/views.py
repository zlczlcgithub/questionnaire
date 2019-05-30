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
                    if str(num+1) in data:
                        result[question.text] = convert_to_answer(data[str(num+1)])
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


def convert_to_answer(answer_num):
    choices = {'1': '満足',
               '2': 'やや満足',
               '3': 'どちらとも言えない',
               '4': 'やや不満',
               '5': '不満'}
    return choices[answer_num]
