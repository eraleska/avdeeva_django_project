from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ['created']

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name_plural = 'Записи'
        ordering = ['-created']

    def __str__(self):
        return self.title
# Create your models here.
