from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'proj_num', 'cpu', 'ram_used', 'ram_percent', 'is_active', 'date_added']
