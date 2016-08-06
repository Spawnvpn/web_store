from django.conf.urls import url
from django.contrib import admin

import goods.views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=goods.views.GoodsListView.as_view(), name='goods_list'),
    url(r'^page/(?P<page>\d+)/$', view=goods.views.GoodsListView.as_view(), name='goods_list'),
    url(r'^goods/(?P<pk>\d+)/$', view=goods.views.GoodsDetailView.as_view(), name='goods_detail'),
    url(r'^shopping-cart/add/$', goods.views.add),
    url(r'^shopping-cart/show/$', goods.views.show),
    url(r'^goods/create/$', view=goods.views.GoodsCreateView.as_view(), name='goods_create'),
    url(r'^goods/(?P<pk>\d+)/update/$', view=goods.views.GoodsUpdateView.as_view(), name='goods_update'),
    url(r'^goods/(?P<pk>\d+)/delete/$', view=goods.views.GoodsDeleteView.as_view(), name='goods_delete'),
]
