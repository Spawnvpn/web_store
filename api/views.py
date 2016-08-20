from django.shortcuts import render
from rest_framework import viewsets, permissions
from goods.models import Product, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from users.models import WebStoreUser
from api.serializers import ProductSerializer, WebStoreUserSerializer, \
    CategorySerializer


@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'products': reverse('product-list', request=request),
        'users': reverse('user-list', request=request),
        'categories': reverse('category-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    model = WebStoreUser
    serializer_class = WebStoreUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WebStoreUser
    serializer_class = WebStoreUserSerializer


class ProductList(generics.ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer




# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class WebStoreUserViewSet(viewsets.ModelViewSet):
#     queryset = WebStoreUser.objects.all()
#     serializer_class = WebStoreUserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
