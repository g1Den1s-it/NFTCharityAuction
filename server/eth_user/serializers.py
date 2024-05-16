from rest_framework import serializers
from .models import User, Captcha

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("public_key", )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "public_key", "profile_image", "email", "first_name", "last_name")



class Captcha(serializers.ModelSerializer):
    class Meta:
        models = ("captcha", )

