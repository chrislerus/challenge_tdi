from django.test import TestCase
from django.test.client import Client
from django.core.files.uploadedfile import SimpleUploadedFile


class UploadTests(TestCase):
    def setUp(self):
        self.factory = Client()
        pass

    def test_basic_upload(self):
        """
        Check that the POST request to upload returns
        the uploaded photo as the response body
        """
        with open('uploads/test_files/test.txt') as fp:
            content_file = fp.read()
            fp.close()
        with open('uploads/test_files/test.txt') as fp:
            response = self.factory.post("/display/", {"pic": fp})
        content_response = response.content

        self.assertEqual(content_file, content_response)