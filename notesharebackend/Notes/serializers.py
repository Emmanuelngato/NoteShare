from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    """def create(self, validated_data):
        # Handle file upload logic here
        # For example, you can save the file to a specific location
        file = validated_data['file']
        # Save the file to a specific location
        # file_path = '/path/to/save/file'
        # with open(file_path, 'wb') as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)
        return validated_data
    """
