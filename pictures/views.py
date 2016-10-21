from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from pictures.models import Picture
from pictures.serializers import PictureSerializer


# Create your views here.

class PictureViewSet(ModelViewSet):

    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)