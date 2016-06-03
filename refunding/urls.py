from django.conf.urls import url
from refunding.views import not_refunded_payments, latest_refunds

urlpatterns = [
    url(r'^payments/$', not_refunded_payments, name='not_refunded_payments'),
    url(r'^refunds/$', latest_refunds, name='latest_refunds'),
]
