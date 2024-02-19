import os

from django.db import models


class File(models.Model):
    class Status(models.TextChoices):
        PENDING_PROCESSING = "pending_processing"
        PROCESSED = "processed"
        FAILED = "failed"

    status = models.CharField(max_length=24, choices=Status.choices, default=Status.PENDING_PROCESSING)
    file = models.FileField(upload_to='uploaded_files/')
    errors = models.JSONField(null=True, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def processed(self) -> bool:
        return self.status == self.Status.PROCESSED

    def get_file_extension(self):
        _, extension = self.file.name.split(".")
        return extension