# Generated by Django 4.2.16 on 2024-10-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articles_make_articles_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='make',
            options={'verbose_name': 'Тип новостей', 'verbose_name_plural': 'Тип новостей'},
        ),
        migrations.AlterField(
            model_name='make',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Тип новостей'),
        ),
    ]