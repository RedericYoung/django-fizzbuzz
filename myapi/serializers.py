from rest_framework import serializers

from .models import Fizz

class FizzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fizz
        fields = ('sport', 'completed', 'id')