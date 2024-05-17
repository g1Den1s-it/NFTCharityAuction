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
                  "goal", "collected", "wallet", "min_price",
                  "owner", "date"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request:
            if 'image' in representation and representation['image']:
                representation['image'] = request.build_absolute_uri(representation['image'])

        return representation

