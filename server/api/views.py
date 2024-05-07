from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import MetadataNFT
from .serializers import MetadataNFTSerialzier
# Create your views here.
class ListAPIViewMetaDataNFT(ListAPIView):
    serializer_class = MetadataNFTSerialzier

    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(MetadataNFT, pk=1)
        serializer = MetadataNFTSerialzier(queryset).data
        return Response(serializer)