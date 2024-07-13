from django.shortcuts import render
from rest_framework import serializers, views, status
from rest_framework.parsers import MultiPartParser
from django.http import FileResponse
from google.cloud import storage
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from google.auth import default
from .serializers import FileUploadSerializer

credentials, project_id = default()
bucket_name ='nyams-noteshare'


class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the uploaded file
        file = serializer.validated_data['file']

        # Create a Cloud Storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket(bucket_name)

        # Create a new blob and upload the file
        blob = bucket.blob(file.name)
        blob.upload_from_file(file)

        # Return a success response
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
    def get(self, request):
        # Create a Cloud Storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket(bucket_name)
        
        # Get the blobs
        blobs = bucket.list_blobs()
    
        # Return the list of blob names
        return Response([blob.name for blob in blobs], status=status.HTTP_200_OK)

class FileDownloaderView(views.APIView):
    
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #Get the file name
        file_name = request.query_params.get('file_name')
        if not file_name:
            return Response({'error': 'File name not provided.'}, status=status.HTTP_400_BAD_REQUEST)

         # Create a Cloud Storage client
        client = storage.Client()
        
        # Get the bucket
        bucket = client.bucket(bucket_name)
    
        # Get the blob
        blob = bucket.blob(file_name)

        # Download the file content
        file_content = blob.download_as_string()

        # Return FileResponse with attachment
        response = FileResponse(file_content, content_type=blob.content_type)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response
