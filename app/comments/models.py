from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, editable=False)
    text = models.TextField(max_length=5000)
    published_on = models.DateTimeField(editable=False)
    content_object = GenericForeignKey('content_type', 'object_id')
    edited = models.BooleanField(default=False)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.published_on = timezone.now()
        super().save(*args, **kwargs)
