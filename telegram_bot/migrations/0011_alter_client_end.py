# Generated by Django 4.1 on 2023-02-22 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0010_auto_20230222_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 22, 15, 31, 51, 717406), null=True, verbose_name='Дата конца тарифа'),
        ),
    ]
