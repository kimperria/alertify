from rest_framework import serializers

from app.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user", "customer_name"]
