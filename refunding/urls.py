from django.conf.urls import url
from refunding import views

urlpatterns = [
    url(r'^refunds/$', views.latest_refunds, name='latest_refunds'),
    url(r'^refunds/new/$', views.new_refund, name='new_refund'),
    url(r'^refunds/(?P<pk>[0-9]+)/edit/$', views.refund_edit, name='refund_edit'),
    url(r'^refunds/(?P<pk>[0-9]+)/delete/$', views.refund_delete, name='refund_delete'),
    url(r'^payments/$', views.not_refunded_payments, name='not_refunded_payments'),
    url(r'^payments/new/$', views.new_payment, name='new_payment'),
    url(r'^payments/(?P<pk>[0-9]+)/edit/$', views.payment_edit, name='payment_edit'),
    url(r'^payments/(?P<pk>[0-9]+)/delete/$', views.payment_delete, name='payment_delete'),
]
