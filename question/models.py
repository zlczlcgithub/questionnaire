from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)

    # TODO: Need to fix db
    '''
    description_for_1 = models.CharField(max_length=200)
    description_for_2 = models.CharField(max_length=200)
    description_for_3 = models.CharField(max_length=200)
    description_for_4 = models.CharField(max_length=200)
    description_for_5 = models.CharField(max_length=200)
    '''
    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.TextField(default='user')
    question = models.TextField(default='question')
    time = models.DateTimeField(default=timezone.now)
    answer = models.TextField()

    def __str__(self):
        return self.answer
