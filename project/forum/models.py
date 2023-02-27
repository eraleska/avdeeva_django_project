from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Themes(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="name_theme",
                            help_text="Название темы")

    class Meta:
        db_table = "Themes"
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __str__(self):
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="name_auth",
                            help_text="Имя автора")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user",
                             help_text="ID пользователя")

    class Meta:
        db_table = "Authors"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="name_news",
                            help_text="Название новости")
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, verbose_name="theme", help_text="ID темы")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="descr",
                            help_text="Описание новости")
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, help_text="ID автора")
    datenews = models.DateTimeField(blank=False, null=False, help_text="Дата публикации", default=datetime(2000,1,1))

    class Meta:
        db_table = "News"
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.name + " | " + str(self.theme.name)






