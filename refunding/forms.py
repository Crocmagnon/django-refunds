from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db.models import Q
from refunding.models import Refund, Payment


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = '__all__'

    payments = forms.ModelMultipleChoiceField(queryset=Payment.objects.none())

    def __init__(self, *args, **kwargs):
        super(RefundForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['payments'].initial = self.instance.payment_set.all()
            self.fields['payments'].queryset = Payment\
                .objects\
                .filter(Q(refund=None) | Q(refund=self.instance))\
                .order_by('-date')

    def save(self, *args, **kwargs):
        # Save the refund
        instance = super(RefundForm, self).save()
        # Remove the refund from payments it was previously assigned to
        self.fields['payments'].initial.update(refund=None)
        # Add the refund to the selected payments
        self.cleaned_data['payments'].update(refund=instance)
        return instance


class RefundFormAdmin(RefundForm):
    class Meta:
        model = Refund
        fields = '__all__'


class RefundFormPublic(RefundForm):
    class Meta:
        model = Refund
        exclude = ('user',)

    date = forms.DateField(
        widget=DateTimePicker(
            options={
                'format': 'YYYY-MM-DD'
            }
        )
    )


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('title', 'value', 'date')
        widgets = {
            'date': DateTimePicker(
                options={
                    "format": "YYYY-MM-DD"
                }
            ),
        }
