from django.shortcuts import render
from .models import Post
from .forms import PostForm
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.DEBUG)


def post_list(request):
    posts = Post.objects.all()
    message = ''
    result = {}
    data = request.POST

    if request.method == 'POST':
        form = PostForm(data)
        if form.is_valid():
            try:
                # user ID
                result["csrfmiddlewaretoken"] = [data["csrfmiddlewaretoken"]]
                for num, question in enumerate(posts):
                    # make a result dict
                    if str(num+1) in data.keys():
                        result[question.text] = convert_to_question(str(num+1))
                    else:
                        result[question.text] = None
                print(result)
            except (KeyError, Post.DoesNotExist):
                return render(request, 'question/post_list.html', {
                    'posts': posts,
                    'message': "投票内容を選んでください",
                })
            df_res = import_df(os.getcwd() + "/question/history_data/")
            df_new = pd.DataFrame.from_dict(result)
            # make a new result while keeping the order of columns
            df_res = df_res.append(df_new, ignore_index=True)[df_new.columns.tolist()]
            df_res.to_csv(os.getcwd() + "/question/history_data/"+"result.csv")
            # save_dict_to_file(result, os.getcwd() + "/question/history_data/" + data["csrfmiddlewaretoken"] + ".txt")
            message = "保存しました"

    return render(request, 'question/post_list.html', {'posts': posts, 'message': message})


def convert_to_question(answer_num):
    choices = {'1': ['満足'],
               '2': ['やや満足'],
               '3': ['どちらとも言えない'],
               '4': ['やや不満'],
               '5': ['不満']}
    return choices[answer_num]


def import_df(path):
    logging.info('Finding a csv file on {}'.format(path))
    if 'result.csv' in os.listdir(path):
        return pd.read_csv(path+'result.csv')
    # make a new df
    else:
        return pd.DataFrame()


def save_dict_to_file(dic, filename):
  f = open(filename,'w')
  f.write(str(dic))
  f.close()
