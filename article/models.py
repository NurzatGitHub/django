from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    title = models.CharField(max_length=255, verbose_name="ФИО")
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Эл. почта")
    salary = models.IntegerField(verbose_name="Зарплата")
    content = models.TextField(blank=True, verbose_name="Роль")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'Персонал'
        ordering = ['time_create','title']

# class Category(models.Model):
#     name = models.CharField(max_length=100,db_index=True)

#     def __str__(self):
#         return self.name