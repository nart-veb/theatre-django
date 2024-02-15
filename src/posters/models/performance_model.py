from django.db import models
from django.utils import timezone


class Performance(models.Model):
    def upload_to(self, file):
        arr = file.split('.')
        ext = arr[-1]
        name = ''
        for i in range(len(arr) - 1):
            name += arr[i]
        time = timezone.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        path = 'images/performances/'
        filename = '{}{}-{}.{}'.format(path, name, time, ext)
        return filename

    producer = models.ForeignKey("posters.Producer", verbose_name="Режиссер", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название спектакля", unique=True)
    acts = models.PositiveIntegerField(verbose_name="Количество актов")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание спектакля", null=True)
    actors = models.ManyToManyField("people.Person", verbose_name="Актёры")
    video_id = models.CharField(max_length=255, verbose_name="Идентификатор ютуб видео", null=True)
    placard = models.ImageField(upload_to=upload_to, verbose_name="Плакат")
    map = models.ForeignKey("posters.Map", on_delete=models.CASCADE, verbose_name="Карта")

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
        path = 'images/performances/'
        filename = '{}{}-{}.{}'.format(path, name, time, ext)
        return filename

    performance = models.ForeignKey(Performance, verbose_name="Спектакль", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

    def __str__(self):
        return str(self.performance)

    class Meta:
        verbose_name = "Изображение спектакля"
        verbose_name_plural = "Изображения спектакля"
