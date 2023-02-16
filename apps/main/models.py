from django.db import models
from django.db.models import QuerySet


class Comics(models.Model):
    """Model for comics"""

    title = models.CharField(
        verbose_name="Название",
        max_length=150,
    )
    published = models.DateField(
        verbose_name='Дата публикации'
    )
    episode = models.IntegerField(
        verbose_name='Серия',
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=1000
    )
    author = models.ManyToManyField(
        to='Author',
        related_name="authors",
        verbose_name="автор"
    )

    class Meta:
        ordering = (
            "-published",
        )
        verbose_name = "комикс"
        verbose_name_plural = "комиксы"


class Author(models.Model):
    """Model for author. """

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=60
    )

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'
    