from django.db.models.query import QuerySet
from . import models
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.

# gere les requetes HTTP pour les objets Friends
class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


# gere les requetes HTTP pour les objects Belonging
class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

#gere les requetes HTTP pour les objets Burrowed
class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]