from web3.auto import w3
import string
import random
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from eth_account.messages import encode_defunct
from rest_framework_simplejwt.tokens import RefreshToken
from .validators import LoginValidator
from .models import User, Captcha

def create_captcha_string():
    letters = string.ascii_lowercase + string.digits
    cryptogen = random.SystemRandom()
    return ''.join(cryptogen.choices(letters, k=42))


class CreateAPIViewEthUser(APIView):

    def post(self, request, *args, **kwargs):
        public_key = request.data.get("public_key")
        user = None

        try:
            user = User.objects.get(public_key=public_key)
            print("second: ", user.public_key)
        except:
            User.objects.create(public_key=public_key).save()



        Captcha.objects.filter(user=user).delete()

        ran_string = create_captcha_string()

        captcha = Captcha(captcha=ran_string,user=user)
        captcha.save()

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
