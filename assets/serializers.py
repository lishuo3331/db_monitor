from rest_framework import serializers
from .models import *





class LinuxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinuxList
        fields = '__all__'

class WindowsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsList
        fields = '__all__'


