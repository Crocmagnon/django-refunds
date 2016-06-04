from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from refunding.forms import RefundForm, RefundFormPublic
from refunding.models import Payment, Refund


@login_required
def not_refunded_payments(request):
    payments = Payment.objects.filter(refund=None)
    sum = payments.aggregate(Sum('value')).get('value__sum') / 100
    context = {
        'payments': payments,
        'sum': sum,
        'default_nothing': 'No payment to be refunded.'
    }
    return render(request, "refunding/payments.html", context)


@login_required
def latest_refunds(request):
    refunds = Refund.objects.all().order_by('date')[:20]
    context = {
        'refunds': refunds,
        'default_nothing': 'No refund to show.'
    }
    return render(request, "refunding/refunds.html", context)


@login_required
def new_refund(request):
    if request.method == 'POST':
        form = RefundFormPublic(request.POST)
        if form.is_valid():
            refund = form.save()
            refund.user = request.user
            refund.save()
            return redirect('latest_refunds')
    else:
        form = RefundFormPublic()

    context = {
        'form': form
    }
    return render(request, "refunding/new_refund.html", context)