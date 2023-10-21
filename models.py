from django.db import models


class Post(models.Model):
    """Модель данных для постов блога
        title - заголовок, slug - метка (для БД), body - тело поста"""
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    
    def __str__(self):
        return self.title
