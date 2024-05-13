from django.urls import path
from .views import ListAPIViewMetaDataNFT, ListAPIViewAuction, RetrieveAPIViewAuction

urlpatterns = [
    path('v1/', ListAPIViewMetaDataNFT.as_view(), name="metadata"),
    path('v1/auction/', ListAPIViewAuction.as_view(), name="list-auction"),
    path('v1/auction/<int:id>/', ListAPIViewAuction.as_view(), name="detail-auction"),
]
