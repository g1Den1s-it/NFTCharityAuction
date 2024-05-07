from django.urls import path
from .views import ListAPIViewMetaDataNFT

urlpatterns = [
    path('v1/', ListAPIViewMetaDataNFT.as_view(), name="metadata"),
]