import os

from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import File


class FileUploadTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('file-list')
        self.upload_url = reverse('file-upload')

    def tearDown(self):
        for file in File.objects.all():
            if default_storage.exists(file.file.name):
                default_storage.delete(file.file.name)
            file.delete()

        super().tearDown()

    def test_file_upload_success(self):
        file = SimpleUploadedFile("testfile.txt", b"abc", content_type="text/plain")
        response = self.client.post(self.upload_url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(File.objects.get().file.name, 'uploaded_files/testfile.txt')

    def test_upload_without_file(self):
        response = self.client.post(self.upload_url, {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["file"], ["No file was submitted."])
        self.assertEqual(File.objects.count(), 0)
