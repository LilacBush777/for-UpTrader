from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('obj', kwargs={'slug': self.slug})