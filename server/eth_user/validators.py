from rest_framework import serializers


class LoginValidator(serializers.Serializer):
    public_key = serializers.CharField()
    signature = serializers.CharField()