from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import filters

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer, ProductsByCategoryListSerializer #ProductsByCategorySerializer


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
        return Response({'cats': cats.title})


class ProductsByCategoryList(APIView):

    @swagger_auto_schema(
        operation_summary='Получить продукты по категориям',
        operation_description='Просто берётся из базы все записи отсортированный по айдишке',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': ProductsByCategoryListSerializer(many=True)},
    )
    def get(self, request):
        title_qp = self.request.query_params.get('title')
        if title_qp:
            category_qs = ProductCategory.objects.filter(title__icontains=title_qp)
        else:
            category_qs = ProductCategory.objects.all()
        srz = ProductsByCategoryListSerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)


class ProductByCategory(APIView):

    @swagger_auto_schema(
        operation_summary='Получить категорию с продуктами',
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type='str'),
        ],
        responses={'200': ProductsByCategoryListSerializer(many=True)},
    )
    def get(self, request, pk):
        category_qs = ProductCategory.objects.filter(pk=pk)
        srz = ProductsByCategoryListSerializer(category_qs, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

