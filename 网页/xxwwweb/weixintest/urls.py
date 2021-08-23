from django.conf.urls import url,include
from weixintest import views

app_name = 'weixintest'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'weixin_id/(\d+)/',views.Button,name='button'),
    url(r'warehousing/(\d+)/$',views.Warehousing,name='warehousing'),
    url(r'warn/(\d+)/$',views.Warn,name='warn'),
    url(r'spider-api/$',views.image_proxy,name='image_proxy'),


]
