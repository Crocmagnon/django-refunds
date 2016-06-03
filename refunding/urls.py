from django.conf.urls import url
from refunding.views import not_refunded_payments

urlpatterns = [
    url(r'^payments/$', not_refunded_payments, name='not_refunded_payments'),
]
