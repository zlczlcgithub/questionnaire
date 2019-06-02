from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)    
    ans1 = models.CharField(max_length=200, default = "非常に不満")
    ans2 = models.CharField(max_length=200, default = "不満")
    ans3 = models.CharField(max_length=200, default = "やや不満")
    ans4 = models.CharField(max_length=200, default = "やや満足")
    ans5 = models.CharField(max_length=200, default = "満足")
    
    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.TextField(default='user')
    question = models.TextField(default='question')
    time = models.DateTimeField(default=timezone.now)
    answer = models.TextField()

    def __str__(self):
        return self.answer
