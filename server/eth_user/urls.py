from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, CreateAPIViewEthUser, ProfileUserApiView


urlpatterns = [
    path('registration/', CreateAPIViewEthUser.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('data/', ProfileUserApiView.as_view(), name='user-profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
