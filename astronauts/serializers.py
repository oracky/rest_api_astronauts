from .models import Astronaut
from rest_framework import serializers


class AstronautSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Astronaut
        fields = ['id', 'name', 'last_name', 'birth_date']