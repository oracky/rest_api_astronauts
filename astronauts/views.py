from rest_framework.response import Response
from django.shortcuts import render
from .models import Astronaut
from rest_framework import viewsets
from astronauts.serializers import AstronautSerializer


class AstronautViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer

    def get_paginated_response(self, data):
        return Response(data)

