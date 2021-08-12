from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        qs = Device.objects.all()
        return qs