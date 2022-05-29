"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from store.views import ProductViewSet, ProductCategoryViewSet, ProductsByCategory, ProductListView
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
print(router.urls)
router1 = routers.DefaultRouter()
router1.register(r'product', ProductViewSet, basename='product')
print(router1.urls)
router2 = routers.DefaultRouter()
router2.register(r'product_cat', ProductCategoryViewSet, basename='product_cat')
print(router2.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router1.urls)),
    path('api/v1/', include(router2 .urls)),
    path('api/v1/products_by_category/', ProductsByCategory.as_view()),
    path('api/v1/product_search/', ProductListView.as_view()),
]
