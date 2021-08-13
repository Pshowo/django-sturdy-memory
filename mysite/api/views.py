from django.contrib.auth.models import User, Group
from rest_framework.response import Response 
from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound
from rest_framework import viewsets
from rest_framework import permissions
from .models import Device
from dashboard.models import Project
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

    def create(self, request, *args, **kwargs):
        token = request.headers['Authenticator'].lstrip("Token ")
        if Project.objects.all().filter(number=request.data['proj_num']).count() > 0:
            proj_token = Project.objects.get(number=request.data['proj_num']).token
            q_token = request.headers['Authenticator'].lstrip("Token ")

            if proj_token == q_token:
                project = Project.objects.get(token=token).number
                dev = Device.objects.create(
                        proj_num=project,
                        cpu=request.data['cpu'],
                        ram_used=request.data['ram_used'],
                        ram_percent=request.data['ram_percent'],
                        is_active=request.data['is_active'])
                serializer = DeviceSerializer(dev, many=False)
                return Response(serializer.data)
            else:
                return Response({"msg": "Unauthorized"}, status=401)
        else:
            return Response({"msg": "Incorrect project number"}, status=404)
            # return HttpResponseNotFound("Wrong project number")