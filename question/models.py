from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    acount_id = models.CharField(max_length=40)
    answer = models.CharField(max_length=2)

    def __str__(self):
        return self.answer