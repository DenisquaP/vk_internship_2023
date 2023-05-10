from django.urls import path, include
from rest_framework import routers
from .views import (
    UsersViewSet,
    get_user_friends,
    delete_friend,
    get_status,
    check_invites,
    send_invite,
    answer_request
)

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:user_id>/friends/', get_user_friends),
    path('users/<int:user_id>/friends/requests/<str:type_of>/', check_invites),  # income/outcome # noqa 501
    path('users/<int:user_id>/friends/<int:friend_id>/delete/', delete_friend),
    path('users/<int:user_id>/friends/<int:friend_id>/status/', get_status),
    path('users/<int:user_id>/friends/<int:friend_id>/send_request/', send_invite),  # noqa 501
    path('users/<int:to_user>/friends/<int:from_user>/answer_request/<str:type_of>/', answer_request),  # noqa 501
]
