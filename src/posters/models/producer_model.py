from django.db import models


class Producer(models.Model):
    """ Модель продюсера. Используется при выводе данных афиши и указании продюсера спектакля. """
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"

    @property
    def full_name(self):
        """
        Полное имя продюсера спектакля
        """
        return f'{self.name[0].capitalize()}. {self.surname}'
