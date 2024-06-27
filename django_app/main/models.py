import os

from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.conf import settings


class VideoData(models.Model):
    id = ShortUUIDField(
        primary_key=True,
        length=settings.SHORT_UUID_LENGTH,
        max_length=settings.SHORT_UUID_LENGTH,
        editable=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256)
    frame_width = models.PositiveSmallIntegerField()
    frame_height = models.PositiveSmallIntegerField()
    fps = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    background_color = models.CharField(max_length=16)
    font = models.PositiveSmallIntegerField()
    font_scale = models.PositiveSmallIntegerField()
    font_thickness = models.PositiveSmallIntegerField()
    font_color = models.CharField(max_length=16)
    file_path = models.CharField(max_length=512)
    file_name = models.CharField(max_length=32)
    file_extension = models.CharField(max_length=16, default='mp4')

    @property
    def file(self):
        return os.path.join(
            self.file_path, f'{self.file_name}.{self.file_extension}'
        )
