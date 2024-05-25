from django.urls import path
from .views import (
        MetaDataNFTRetrieveAPIView,
        ListAPIViewAuction,
        RetrieveAPIViewAuction,
        StatisticDataApiView,
    )

urlpatterns = [
    path('v1/<int:id>/', MetaDataNFTRetrieveAPIView.as_view(), name="metadata"),
    path('v1/auction/', ListAPIViewAuction.as_view(), name="list-auction"),
    path('v1/auction/<int:id>/', RetrieveAPIViewAuction.as_view(), name="detail-auction"),
    path('v1/statistic/', StatisticDataApiView.as_view(), name="statistic"),
]
