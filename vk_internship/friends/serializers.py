from rest_framework import serializers
from .models import (
    Friends,
    Invites,
    Users
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


class InviteSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Invites
        fields = '__all__'
