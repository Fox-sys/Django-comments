from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Post(models.Model):
    name = models.CharField('название поста', max_length=150)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField('текст', max_length=25000)
    comments = models.ManyToManyField('comments.Comment', blank=True)
    published_on = models.DateTimeField('Опубликованно', editable=False)
    edited = models.BooleanField('Редактировалось ли', default=False)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.published_on = timezone.now()
        super().save(*args, **kwargs)
