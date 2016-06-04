from django.conf.urls import url
from refunding import views

urlpatterns = [
    url(r'^payments/$', views.not_refunded_payments, name='not_refunded_payments'),
    url(r'^refunds/$', views.latest_refunds, name='latest_refunds'),
    url(r'^refunds/new/$', views.new_refund, name='new_refund'),
    url(r'^refunds/(?P<pk>[0-9]+)/edit/$', views.refund_edit, name='refund_edit'),
]
