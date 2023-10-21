from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Модель данных для постов блога
        title - заголовок, slug - метка (для БД), body - тело поста"""

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLICHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title
