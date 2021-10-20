from rest_framework.serializers import Serializer, FileField, ListField,ModelSerializer
from train.models import ModelClass

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(Serializer):
    file_uploaded = ListField(child=FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False ))

    class Meta:
        fields = ['file_uploaded']

class TrainSerializer(ModelSerializer):
    class Meta:
        model = ModelClass
        fields = '__all__'


    

