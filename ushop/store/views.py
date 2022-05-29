from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import filters

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer, ProductByCategorySerializer


class ProductViewSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    pagination_class = ProductViewSetPagination

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = ProductCategory.objects.get(pk=pk)
        return Response({'cats': cats.name})


class ProductsByCategory(APIView):

    def get(self, request):
        category_qs = ProductCategory.objects.all()
        srz = ProductByCategorySerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

