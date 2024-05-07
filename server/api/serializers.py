from rest_framework import serializers
from .models import MetadataNFT


class MetadataNFTSerialzier(serializers.ModelSerializer):
    class Meta:
        model = MetadataNFT
        fields = ['name', 'description', 'image']