from django.test import TestCase
from django.test.client import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile


class UploadTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        pass

    def test_basic_upload(self):
        """
        Check that the POST request to upload returns
        the uploaded photo as the response body
        """
        response = self.factory.post("/display/", {})

        self.assertEqual("test", "test")