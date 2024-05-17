from base64 import b64decode

from web3.auto import w3
import string
import random
import jwt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from eth_account.messages import encode_defunct
from rest_framework_simplejwt.tokens import RefreshToken
from .validators import LoginValidator
from .serializers import UserProfileSerializer
from .models import User, Captcha


def create_captcha_string():
    letters = string.ascii_lowercase + string.digits
    cryptogen = random.SystemRandom()
    return ''.join(cryptogen.choices(letters, k=42))


class CreateAPIViewEthUser(APIView):

    def post(self, request, *args, **kwargs):
        public_key = request.data.get("public_key")

        user, created_user = User.objects.get_or_create(public_key=public_key)

        ran_string = create_captcha_string()

        captcha, created_captcha = Captcha.objects.update_or_create(user=user, defaults={'captcha': ran_string})

        return Response({'captcha': captcha.captcha})


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        validator = LoginValidator(data=request.data)
        public_key = request.data.get("public_key")
        signature = request.data.get("signature")

        if validator.is_valid():
            if User.objects.filter(public_key=public_key).exists():
                user = get_object_or_404(User, public_key=public_key)
                if Captcha.objects.filter(user=user).exists():
                    captcha = get_object_or_404(Captcha, user=user)

                    message = encode_defunct(text=captcha.captcha)

                    key = w3.eth.account.recover_message(signable_message=message, signature=signature)

                    if user.public_key == key:
                        refresh_token = RefreshToken.for_user(user)
                        return Response({
                            "refresh": str(refresh_token),
                            "access": str(refresh_token.access_token)
                        })

                    return Response({'message': "The signature does not match the user"})
                return Response({'message': "User doesn't have captcha"})
            return Response({'message': "Not valid public key or signature"})
        return Response({'message': "public key and signature required"})


class ProfileUserApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserProfileSerializer(user)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user_id = request.user.id

        try:
            user = User.objects.get(id=user_id)

            user.update(**request.data)
            user.refresh_from_db()

            serializer = UserProfileSerializer(user)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
