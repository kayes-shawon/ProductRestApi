from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )