from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Banda

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BandaSerializer(serializers.ModelSerializer):
    membros = UserSerializer(many=True)
    usuario = UserSerializer()

    class Meta:
        model = Banda
        fields = '__all__'
