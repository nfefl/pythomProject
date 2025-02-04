from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория музыки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория музыки'
        verbose_name_plural = 'Категория музыки'


class Articles(models.Model):
    tittle = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Время')
    make = models.ForeignKey(Make, on_delete=models.CASCADE, verbose_name='Тип')


    def __str__(self):
        return f'{self.make}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

class INews(models.Model):
    tittle = models.CharField('Название', max_length=50, default='Важно')
    anons = models.CharField('Анонс', max_length=250, default='Важно')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Время')

    def __str__(self):
        return self.anons

    class Meta:
        verbose_name = "Важную новость"
        verbose_name_plural = 'Важные Новости'


