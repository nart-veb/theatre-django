from django.db import models
from django.urls import reverse


class Poster(models.Model):
    performance = models.ForeignKey("posters.Performance", on_delete=models.CASCADE, verbose_name="Спектакль")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    close_date = models.DateTimeField(verbose_name="Дата закрытия онлайн бронирования")

    def __str__(self):
        return self.performance

    def get_absolute_url(self):
        return reverse("poster:poster_detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиши"

    @property
    def formatted_start_date(self):
        return self.start_date.strftime('%d.%m / %H:%M')

    @property
    def time(self):
        return self.start_date.strftime('%H:%M')


