from uuid import uuid4
from django.utils import timezone


def upload_to(instance, filename):
    """
    Uploads file to ...
    """
    class_name = instance.__class__.__name__.lower()
    file, ext = filename.split('.')
    new_filename = uuid4()

    time = timezone.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = f'/media/{class_name}/images/'
    filename = f"{path}{new_filename}-{time}.{ext}"
    return filename
