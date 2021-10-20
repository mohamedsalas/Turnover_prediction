from rest_framework.serializers import Serializer, FileField, ListField,ChoiceField
import os

# Serializers define the API representation.
#class UploadSerializer(Serializer):
    #Upload_Image = FileField()
    #Class_Name = ChoiceField(choices=os.listdir("./facenet/myclassifier/"))

 #   class Meta:
 #       fields = ['Class_Name','Upload_Image']


# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(Serializer):
    
    file_uploaded = ListField(FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False ))

    class Meta:
        fields = ['file_uploaded']
