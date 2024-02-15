from django.urls import reverse
from django.db import models
from django.utils import timezone

from utils.uploaders import upload_to


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

        """
        return f'{self.name[0].capitalize()}. {self.surname}'


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


class Performance(models.Model):
    producer = models.ForeignKey(Producer, verbose_name="Режиссер", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название спектакля", unique=True)
    acts = models.PositiveIntegerField(verbose_name="Количество актов")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание спектакля", null=True)
    actors = models.ManyToManyField("people.Person", verbose_name="Актёры")
    video_id = models.CharField(max_length=255, verbose_name="Идентификатор ютуб видео", null=True)
    placard = models.ImageField(upload_to=upload_to, verbose_name="Плакат")
    map = models.ForeignKey(Map, on_delete=models.CASCADE, verbose_name="Карта")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"


class PerformanceImage(models.Model):

    def upload_to(self, file):
        arr = file.split('.')
        ext = arr[-1]
        name = ''
        for i in range(len(arr) - 1):
            name += arr[i]
        time = timezone.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        path = 'images/perfomances/'
        filename = '{}{}-{}.{}'.format(path, name, time, ext)
        return filename

    perfomance = models.ForeignKey(Perfomance, verbose_name="Спектакль", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

    def __str__(self):
        return str(self.perfomance)

    class Meta:
        verbose_name = "Изображение спектакля"
        verbose_name_plural = "Изображения спектакля"


class Poster(models.Model):
    perfomance = models.ForeignKey(Performance, on_delete=models.CASCADE, verbose_name="Спектакль")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    close_date = models.DateTimeField(verbose_name="Дата закрытия онлайн бронирования")

    def __str__(self):
        return str(self.perfomance)

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


class Ticket(models.Model):
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE, verbose_name="Афиша")
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
