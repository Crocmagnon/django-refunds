from django.contrib import admin
from refunding.models import Refund, Payment


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')
    list_display_links = ('title',)
    search_fields = ('title',)
    date_hierarchy = 'date'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'value', 'user', 'refund')
    list_display_links = ('title',)
    search_fields = ('title',)
    date_hierarchy = 'date'
