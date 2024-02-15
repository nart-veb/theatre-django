from django.db import models
from django.utils import timezone


class Map(models.Model):
    def upload_to(self, file):
        arr = file.split('.')
        ext = arr[-1]
        name = ''
        for i in range(len(arr) - 1):
            name += arr[i]
        time = timezone.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        path = 'maps/' if ext == 'svg' else 'json/'
        filename = '{}{}-{}.{}'.format(path, name, time, ext)
        return filename

    map_svg = models.FileField(verbose_name="Схема SVG", upload_to=upload_to)
    seats_json = models.FileField(verbose_name="Места JSON", upload_to=upload_to)

    def __str__(self):
        return str(self.map_svg)

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"
