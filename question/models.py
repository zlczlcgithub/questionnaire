from django.db import models

CHOICES = [('1', '満足'),
           ('2', 'やや満足'),
           ('3', 'どちらとも言えない'),
           ('4', 'やや不満'),
           ('5', '不満')]


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer = models.TextField()
    
    def __str__(self):
        return self.answer