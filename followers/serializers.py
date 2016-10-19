from django.contrib.auth.models import User
from rest_framework import serializers

from followers.models import Relationship


class RelationshipUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        read_only_fields = ('origin',)

    def validate_target(self, value):
        # try:
        #     User.objects.get(pk=value)
        # except User.DoesNotExist:
        #     raise serializers.ValidationError("User does not exist")
        return value

    def validate(self, attrs):
        request_user = self.context.get("request").user
        if request_user == attrs.get('target'):
            raise serializers.ValidationError("You can not follow yourself")
        if Relationship.objects.filter(origin=request_user, target=attrs.get('target')).exists():
            raise serializers.ValidationError("You are already following this user")
        return attrs
