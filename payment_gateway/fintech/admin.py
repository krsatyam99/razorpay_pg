from django.contrib import admin
from fintech.models import PaymentRecord


class payment_Admin(admin.ModelAdmin):
    list_display = ('id','order_id', 'status', 'created_at')
admin.site.register(PaymentRecord,payment_Admin)