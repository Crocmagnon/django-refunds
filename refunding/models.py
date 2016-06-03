from django.db import models
from django.conf import settings
from django.db.models import Sum

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Refund(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def eur_value(self) -> float:
        return self.payment_set.all().aggregate(Sum('value')).get('value__sum') / 100

    def __str__(self) -> str:
        return "{0} on {1} for {2}".format(self.title, self.date, self.eur_value())


class Payment(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    refund = models.ForeignKey(
        Refund,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return '{0} on {1} for {2}'.format(self.title, self.date, self.value / 100)

    def eur_value(self) -> float:
        return self.value / 100
