from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import MetadataNFT, Auction
from .serializers import MetadataNFTSerialzier, AuctionSerializer


# Create your views here.
class ListAPIViewMetaDataNFT(ListAPIView):
    """view get metadate of current nft-token"""
    serializer_class = MetadataNFTSerialzier

    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(MetadataNFT, pk=1)
        serializer = MetadataNFTSerialzier(queryset).data
        return Response(serializer)


class ListAPIViewAuction(ListAPIView):
    """get list of all data of open auction from database"""
    queryset = Auction.objects.filter(is_open=True)
    serializer_class = AuctionSerializer

class RetrieveAPIViewAuction(RetrieveAPIView):
    """get data of detail of auction"""
    queryset = Auction.objects.filter(is_open=True)
    serializer_class = AuctionSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)

        auction = self.get_queryset().filter(id=id)
        serializer = AuctionSerializer(auction).data

        return Response(serializer)
