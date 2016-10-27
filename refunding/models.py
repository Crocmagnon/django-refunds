from django.db import models
from django.conf import settings
from django.db.models import Sum

import logging
logger = logging.getLogger(__name__)

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Refund(models.Model):
    class Meta:
        verbose_name = 'remboursement'
        verbose_name_plural = 'remboursements'

    title = models.CharField(max_length=100, verbose_name='titre')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        verbose_name='utilisateur'
    )

    def eur_value(self) -> float:
        value_sum = self.payment_set.all().aggregate(Sum('value')).get('value__sum')
        if value_sum:
            return value_sum / 100
        else:
            return 0

    def __str__(self) -> str:
        return "{0} le {1} pour {2:.2f}".format(self.title, self.date, self.eur_value())


class Payment(models.Model):
    class Meta:
        verbose_name = 'paiement'
        verbose_name_plural = 'paiements'

    title = models.CharField(max_length=100, verbose_name='titre')
    date = models.DateField()
    value = models.IntegerField(verbose_name='valeur')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='utilisateur'
    )
    refund = models.ForeignKey(
        Refund,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='remboursement'
    )

    def __str__(self) -> str:
        s = '{0} le {1} pour {2:.2f}'.format(self.title, self.date, self.value / 100)
        logger.error(s)
        return s

    def eur_value(self) -> float:
        return self.value / 100
