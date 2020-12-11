from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    summary = models.TextField(default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '게시물'


class Comment(models.Model):
    summary = models.TextField(default='')
    notice_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '댓글'
