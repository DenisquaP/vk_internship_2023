from rest_framework.decorators import api_view
from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Friends,
    Invites,
    Users
)
from .serializers import (
    UserSerializer,
    FriendSerializer,
    InviteSerializer
)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
def get_user_friends(request, user_id):
    data = Friends.objects.filter(user_id=user_id)
    serializer = FriendSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_friend(request, user_id, friend_id):
    if Friends.objects.filter(user=user_id, friend=friend_id):
        Friends.objects.filter(user=user_id, friend=friend_id)[0].delete()
        Friends.objects.filter(user=friend_id, friend=user_id)[0].delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'message': 'You`re not friends'})


@api_view(['GET'])
def get_status(request, user_id, friend_id):
    if user_id == friend_id:
        return Response({'message': 'it`s you'})
    friendship = Friends.objects.filter(user=user_id, friend=friend_id)
    income = Invites.objects.filter(from_user=user_id, to_user=friend_id)
    outcome = Invites.objects.filter(from_user=friend_id, to_user=user_id)
    if friendship:
        return Response({'message': 'friend'})
    elif income:
        return Response({'message': 'income friendship request'})
    elif outcome:
        return Response({'message': 'outcome friendship request'})

    return Response({'message': 'nothing'})


@api_view(['GET'])
def check_invites(request, user_id, type_of):
    user = Users.objects.get(pk=user_id)
    if type_of == 'incoming':
        data = Invites.objects.filter(to_user=user)
        serializer = InviteSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = Invites.objects.filter(from_user=user)
    serializer = InviteSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def send_invite(request, user_id, friend_id):
    if Users.objects.filter(pk=friend_id):
        user = Users.objects.get(pk=user_id)
        friend = Users.objects.get(pk=friend_id)

        have_incoming = Invites.objects.filter(
            from_user=friend,
            to_user=user
            )
        have_outcoming = Invites.objects.filter(
            from_user=user,
            to_user=friend
            )

        if user_id == friend_id:
            return Response(
                {'message': 'You can`t send invite to yourself'},
                status=status.HTTP_400_BAD_REQUEST
                )
        elif have_incoming:
            have_incoming[0].delete()
            Friends.objects.create(user=user, friend=friend)
            Friends.objects.create(user=friend, friend=user)
            return Response({
                'message': 'Now you are friends, because you have incoming request from this user'  # noqa 501
            }, status=status.HTTP_200_OK)
        elif have_outcoming:
            return Response({'message': 'You have already sanded a request'})

        Invites.objects.create(from_user=user, to_user=friend)
        return Response({
                'message': 'A request was sanded'  # noqa 501
            }, status=status.HTTP_200_OK)
    return Response({'message': 'User does not exists'})


@api_view(["POST"])
def answer_request(request, from_user, to_user, type_of):
    user1 = Users.objects.get(pk=from_user)
    user2 = Users.objects.get(pk=to_user)
    invite = Invites.objects.filter(from_user=user1, to_user=user2)

    if invite:
        invite[0].delete()
        if type_of == 'accept':
            Friends.objects.create(user=user1, friend=user2)
            Friends.objects.create(user=user2, friend=user1)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)
