from django import forms
from refunding.models import Refund, Payment


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = '__all__'

    payments = forms.ModelMultipleChoiceField(queryset=Payment.objects.all())

    def __init__(self, *args, **kwargs):
        super(RefundForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['payments'].initial = self.instance.payment_set.all()

    def save(self, *args, **kwargs):
        # Save the refund
        instance = super(RefundForm, self).save(commit=False)
        # Remove the refund from payments it was previously assigned to
        self.fields['payments'].initial.update(refund=None)
        # Add the refund to the selected payments
        self.cleaned_data['payments'].update(refund=instance)
        return instance
