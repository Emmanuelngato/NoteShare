from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch, MagicMock
from google.cloud import storage

class FileUploadViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    @patch('google.cloud.storage.Client')
    def test_file_upload_success(self, mock_client):
        # Mock the Cloud Storage client and bucket
        mock_bucket = MagicMock()
        mock_client.return_value.bucket.return_value = mock_bucket

        # Mock the uploaded file
        mock_file = MagicMock()
        mock_file.name = 'test_file.txt'
        mock_file.content_type = 'text/plain'
        mock_file.size = 100
        mock_file.read.return_value = b'This is a test file content'

        # Mock the serializer
        mock_serializer = MagicMock()
        mock_serializer.validated_data = {'file': mock_file, 'subject': 'Test Subject'}
        mock_serializer.is_valid.return_value = True

        # Patch the serializer class
        with patch('Notes.views.FileSerializer', return_value=mock_serializer):
            # Make a POST request to the API endpoint
            response = self.client.post('/api/file-upload/', {'file': mock_file, 'subject': 'Test Subject'}, format='multipart')

        # Assert the response status code and message
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'message': 'File uploaded successfully.'})

        # Assert that the file was uploaded to the Cloud Storage bucket with the correct metadata
        mock_bucket.blob.assert_called_once_with('test_file.txt')
        mock_bucket.blob.return_value.upload_from_string.assert_called_once_with(b'This is a test file content', metadata={
            'uploaded_by': self.user.username,
            'content_type': 'text/plain',
            'size': 100,
            'subject': 'Test Subject'
        })

    def test_file_upload_unauthenticated(self):
        # Make a POST request to the API endpoint without authentication
        response = self.client.post('/api/file-upload/', {'file': 'test_file.txt', 'subject': 'Test Subject'}, format='multipart')

        # Assert the response status code and message
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})
