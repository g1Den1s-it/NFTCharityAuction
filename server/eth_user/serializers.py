from rest_framework import serializers
from .models import User, Captcha

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("public_key", )


class Captcha(serializers.ModelSerializer):
    class Meta:
        models = ("captcha", )

