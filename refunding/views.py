from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from refunding.forms import RefundFormPublic, PaymentForm
from refunding.models import Payment, Refund


#############################
# -------- Refunds -------- #
#############################


@login_required
def latest_refunds(request):
    refunds = Refund.objects.all().order_by('-date')[:20]
    context = {
        'refunds': refunds,
        'default_nothing': 'No refund to show.'
    }
    return render(request, "refunding/refunds.html", context)


@login_required
@permission_required('refunding.add_refund')
def new_refund(request):
    if request.method == 'POST':
        form = RefundFormPublic(request.POST)
        if form.is_valid():
            refund = form.save()
            refund.user = request.user
            refund.save()

            messages.success(request, 'Refund created successfully')
            return redirect('latest_refunds')
    else:
        form = RefundFormPublic()

    context = {
        'form': form,
        'title': 'New refund'
    }

    return render(request, "refunding/refund_payment_detail.html", context)


@login_required
@permission_required('refunding.change_refund')
def refund_edit(request, pk):
    refund = get_object_or_404(Refund, pk=pk)

    if request.method == 'POST':
        form = RefundFormPublic(request.POST, instance=refund)
        if form.is_valid():
            refund = form.save()
            refund.user = request.user
            refund.save()

            messages.success(request, 'Refund edited successfully')
            return redirect('latest_refunds')
    else:
        form = RefundFormPublic(instance=refund)

    context = {
        'form': form,
        'title': 'Edit refund',
        'refund': refund
    }

    return render(request, 'refunding/refund_payment_detail.html', context)


@login_required
@permission_required('refunding.delete_refund')
def refund_delete(request, pk):
    refund = get_object_or_404(Refund, pk=pk)

    refund.delete()

    messages.success(request, "Refund deleted successfully")

    return latest_refunds(request)


##############################
# -------- Payments -------- #
##############################


@login_required
def not_refunded_payments(request):
    payments = Payment.objects.filter(refund=None).order_by('-date')
    value_sum = payments.aggregate(Sum('value')).get('value__sum')
    if value_sum:
        value_sum /= 100
    else:
        value_sum = 0

    context = {
        'payments': payments,
        'sum': value_sum,
        'default_nothing': 'Nothing to refund :)'
    }
    return render(request, "refunding/payments.html", context)


@login_required
@permission_required('refunding.add_payment')
def new_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()

            messages.success(request, 'Payment created successfully')
            return redirect('not_refunded_payments')
    else:
        form = PaymentForm()

    context = {
        'form': form,
        'title': 'New payment'
    }

    return render(request, "refunding/refund_payment_detail.html", context)


@login_required
@permission_required('refunding.change_payment')
def payment_edit(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()

            messages.success(request, 'Payment edited successfully')
            return redirect('not_refunded_payments')
    else:
        form = PaymentForm(instance=payment)

    context = {
        'form': form,
        'title': 'Edit payment',
        'payment': payment
    }

    return render(request, 'refunding/refund_payment_detail.html', context)


@login_required
@permission_required('refunding.delete_payment')
def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    payment.delete()

    messages.success(request, "Payment deleted successfully")

    return not_refunded_payments(request)


@login_required
def already_refunded_payments(request):
    refunded = Payment.objects.exclude(refund=None).order_by('-date', '-id')
    value_sum = refunded.aggregate(Sum('value')).get('value__sum')
    if value_sum:
        value_sum /= 100
    else:
        value_sum = 0

    context = {
        'refunded': refunded,
        'sum': value_sum,
        'default_nothing': 'No refunded payment :)'
    }
    return render(request, "refunding/refunded_payments.html", context)
