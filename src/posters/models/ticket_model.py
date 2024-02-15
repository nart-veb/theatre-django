from django.db import models


class Ticket(models.Model):
    poster = models.ForeignKey('posters.Poster', on_delete=models.CASCADE, verbose_name="Афиша")
    seat_id = models.PositiveIntegerField()
    row_number = models.PositiveIntegerField(verbose_name="Ряд")
    seat_number = models.PositiveIntegerField(verbose_name="Место")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    sector = models.CharField(max_length=50, verbose_name="Сектор")
    reservation = models.BooleanField(default=False, verbose_name="Забронирован")

    def __str__(self):
        return str(self.poster)

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
