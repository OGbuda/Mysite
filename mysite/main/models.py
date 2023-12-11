from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Download(models.Model):
    name = models.CharField('Название', max_length=35)
    description = models.TextField('Описание', default='')
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, default=None, null=True, blank=True)
    content = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )

    def  __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видосики'

