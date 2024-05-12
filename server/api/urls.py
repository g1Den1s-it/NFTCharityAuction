from django.urls import path
from .views import ListAPIViewMetaDataNFT, ListAPIViewAuction

urlpatterns = [
    path('v1/', ListAPIViewMetaDataNFT.as_view(), name="metadata"),
    path('v1/aution/', ListAPIViewAuction.as_view(), name="list-auction"),
]
