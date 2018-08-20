
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table  = 'my_post'#데이터베이스 테이블에서 이름을 정의, 지정 안하면 appname_classname 된다.
        ordering  = ('modify_date',)

    def __str__(self):
        return self.content


    def save(self, *args, **kwargs):#객체의 내용을 데이터베이스에 저장
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',  on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField()


    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.owner.username})'