from rest_framework import serializers
from .models import MetadataNFT, Auction


class MetadataNFTSerialzier(serializers.ModelSerializer):
    class Meta:
        model = MetadataNFT
        fields = ['name', 'description', 'image']


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ["id", "name", "description", "image",
                  "goal", "collected", "min_price",
                  "owner", "date"]
