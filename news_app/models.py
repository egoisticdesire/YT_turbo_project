from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(
        verbose_name='Наименование',
        max_length=150,
    )
    content = models.TextField(
        verbose_name='Текст новости',
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='img/%Y/%m/%d/',
        blank=True,
    )
    is_published = models.BooleanField(
        verbose_name='Активность',
        default=True,
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.PROTECT,
        # related_name='get_news',
    )
    views = models.IntegerField(
        verbose_name='Просмотры',
        default=0,
    )

    def get_absolute_url(self):
        return reverse_lazy(
            'view_news',
            kwargs={'pk': self.pk},
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(
        verbose_name='Категория',
        max_length=150,
        db_index=True,
    )

    def get_absolute_url(self):
        return reverse_lazy(
            'category',
            kwargs={'category_id': self.pk},
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
