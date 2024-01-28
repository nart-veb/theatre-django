from django.db import models
from datetime import datetime


class Press(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/press/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  name = models.CharField(max_length=255, verbose_name="Заголовок")
  text = models.TextField(verbose_name="Текст статьи")
  url = models.URLField(max_length=255,verbose_name="Ссылка на источник")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение", blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Пресса'
    verbose_name_plural = 'Пресса'
