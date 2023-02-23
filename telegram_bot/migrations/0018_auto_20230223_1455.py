# Generated by Django 3.2.12 on 2023-02-23 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0017_auto_20230223_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл к заказу', 'verbose_name_plural': 'Файлы к заказу'},
        ),
        migrations.AddField(
            model_name='file',
            name='file_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на файл'),
        ),
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 23, 14, 55, 6, 423003), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 14, 55, 6, 423002), verbose_name='Опубликован'),
        ),
    ]
