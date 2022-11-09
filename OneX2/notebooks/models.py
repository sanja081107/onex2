from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['title']


class Notebook(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True, verbose_name='title')
    depth = models.FloatField(verbose_name='depth')
    diagonal = models.FloatField(verbose_name='diagonal')
    height = models.FloatField(verbose_name='height')
    width = models.FloatField(verbose_name='width')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='brand', related_name='notebooks')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'
