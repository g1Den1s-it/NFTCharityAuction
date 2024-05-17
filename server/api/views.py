from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from web3 import Web3
from eth_user.models import User
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
        pk = kwargs.get('id', 1)
        self.queryset = self.get_queryset().get(id=pk)

        if self.queryset.is_open == True:
            serializer = AuctionSerializer(self.get_queryset(), context={'request': request}).data
            return Response(serializer)

        return Response({})


class StatisticDataApiView(GenericAPIView):
    """general statistic of users, NFTs, closed auction and
    amount of money collected.Data will update every 24 hours"""

    @method_decorator(cache_page(86400))
    def get(self, request, *args, **kwargs):
        users = User.objects.count()
        auctions = Auction.objects.filter(is_open=False)
        collected = 0
        web3 = Web3(Web3.HTTPProvider("http://network:8545"))
        for auction in auctions:
            collected += web3.from_wei(
                web3.eth.get_balance(auction.wallet),
                "ether"
            )
        return Response(
            {
                "users": users,
                "gifted_nfts": 0,
                "closed_auctions": auctions.count(),
                "money_collected": collected
            }
        )
