from django.db import models

from app.abstract import TimeStampedModel
from app.customers.models import Customer


class Order(TimeStampedModel):
    item = models.CharField(max_length=150)
    amount = models.PositiveIntegerField()
    customer = models.ForeignKey(
        Customer, related_name="customer_orders", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Order for {self.customer.customer_name}: {self.item}"
