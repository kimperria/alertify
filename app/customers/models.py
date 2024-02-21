from django.contrib.auth.models import User
from django.db import models

from app.abstract import TimeStampedModel


def generate_unique_customer_code():
    # Get the latest customer code from the DB
    lastest_customer = Customer.objects.order_by("-customer_code").first()

    if lastest_customer:
        # Exctract the numeric part fo the code and incremeent
        code_number = int(lastest_customer.customer_code[1:]) + 1
    else:
        # First customer
        code_number = 1
    # Format the code with leading zeros and the 'C' prefix
    customer_code = "C" + str(code_number).zfill(5)

    return customer_code


class Customer(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=6, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)

    def save(self, *args, **kwargs):
        # Generate  unique customer code before saving
        if not self.customer_code:
            self.customer_code = generate_unique_customer_code()
        super().save(*args, **kwargs)

    def __str__(self):
        # return f"{self.customer_code}  {self.customer_name}"
        return self.user.username
