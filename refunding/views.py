from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from refunding.models import Payment


@login_required
def not_refunded_payments(request):
    payments = Payment.objects.filter(refund=None)
    sum = payments.aggregate(Sum('value')).get('value__sum') / 100
    context = {
        'payments': payments,
        'sum': sum,
        'default_nothing': 'No payment to be refunded.'
    }
    return render(request, "refunding/payments_list.html", context)
