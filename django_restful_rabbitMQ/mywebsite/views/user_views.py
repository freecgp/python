from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from mywebsite.permissions import IsOwnerOrReadOnly
from mywebsite.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)