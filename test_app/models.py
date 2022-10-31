from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey


class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        return reverse_lazy(
            'rubric',
            kwargs={'pk': self.pk},
        )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Article(models.Model):
    name = models.CharField(
        max_length=50,
    )
    category = TreeForeignKey(
        Rubric, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
