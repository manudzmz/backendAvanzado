from rest_framework.serializers import ModelSerializer

from pictures.models import Picture


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        read_only_fields = ('owner',)