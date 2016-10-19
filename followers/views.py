from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from followers.serializers import RelationshipUserSerializer
from followers.utils import get_following


class FollowingViewSet(ListModelMixin, GenericViewSet):
    serializer_class = RelationshipUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_following(self.request.user)

    # Al añadir herencia de ListModelMixin no hace falta este parrafo
    # def list(self, request):
    #     following = get_following(request.user)
    #     serializer = RelationshipUserSerializer(following, many=True)
    #     return Response(serializer.data)
