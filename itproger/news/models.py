from django.db import models

class Articles(models.Model):
    tittle = models.CharField('Название', max_length=50, default='Cpa')
    anons = models.CharField('Анонс', max_length=250, default='Чтото')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Время')

    def __str__(self):
        return self.tittle
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
# Create your models here.
