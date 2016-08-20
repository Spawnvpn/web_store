from api.serializers import ProductSerializer, WebStoreUserSerializer, \
    CategorySerializer
from django.conf.urls import include, url
from goods.models import Product, Category
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from users.models import WebStoreUser

# router = DefaultRouter()
# router.register(r'products', views.ProductViewSet)
# router.register(r'users', views.WebStoreUserViewSet)

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^products/$', view=views.ProductList.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer), name='product-list'),
    url(r'^products/(?P<pk>\d+)/$', view=views.ProductDetail.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer), name='product-detail'),
    url(r'^users/$', view=views.UserList.as_view(queryset=WebStoreUser.objects.all(), serializer_class=WebStoreUserSerializer), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', view=views.UserDetail.as_view(queryset=WebStoreUser.objects.all(), serializer_class=WebStoreUserSerializer), name='user-detail'),
    url(r'^categories/$', view=views.CategoryList.as_view(queryset=Category.objects.all(), serializer_class=CategorySerializer), name='category-list'),
    url(r'^categories/(?P<pk>\d+)/$', view=views.CategoryDetail.as_view(queryset=Category.objects.all(), serializer_class=CategorySerializer), name='category-detail'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
