from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Tariff(models.Model):

    title = models.CharField(
        unique=True,
        max_length=256,
        verbose_name='Название тарифа'
    )
    request_quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество заявок'
    )
    price = models.PositiveBigIntegerField(
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.title


class Administrator(models.Model):

    full_name = models.CharField(
        max_length=256,
        verbose_name='Полное имя'
    )
    chat_id = models.PositiveBigIntegerField(
        verbose_name='ID чата в ТГ'
    )

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f'{self.full_name}: {self.chat_id}'


class Client(models.Model):

    chat_id = models.PositiveBigIntegerField(
        verbose_name='ID чата в ТГ'
    )
    tariff = models.ForeignKey(
        null=True,
        to=Tariff,
        on_delete=models.SET_NULL,
        verbose_name='Тариф'
    )
    requests_left = models.PositiveSmallIntegerField(
        verbose_name='Кол-во оставшихся запросов'
    )
    end = models.DateField(
        null=True,
        blank=True,
        default=datetime.today() + relativedelta(months=1),
        verbose_name='Дата конца тарифа'
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.chat_id} - {self.tariff}'


class Freelancer(models.Model):

    chat_id = models.PositiveBigIntegerField(
        verbose_name='ID чата в ТГ'
    )

    class Meta:
        verbose_name = 'Подрядчик'
        verbose_name_plural = 'Подрядчики'