from django.db import models

# Create your models here.
class PaymentRecord(models.Model): 
    order_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=100, null=True)
    currency = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment Record #{self.pk}"  