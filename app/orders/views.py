from decouple import config
from django.shortcuts import get_object_or_404
from rest_framework import (
    permissions,
    status,
    viewsets,
)
from rest_framework.response import Response
from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from app.customers.models import Customer
from app.orders.models import Order
from app.orders.serializers import OrderSerializer

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
phone_number = config("TWILLIO_PHONE_NUMBER")
client = Client(account_sid, auth_token)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "put", "patch", "post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        try:
            customer_id = request.data.get("customer")

            customer = get_object_or_404(Customer, pk=customer_id)

            client_phone_number = customer.phone_number

            client_user_name = customer.user.username

            message = client.messages.create(
                body=f'"Ahoy {client_user_name}! Your order has been successfully placed on Kimperria-Alertify services. Best: Admin, Kimperria"',
                from_=phone_number,
                to=client_phone_number,
            )

            print("Message", message)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except TwilioException as e:
            print(f"Failed to send SMS: {e}")
            body = {
                "status": e.status,
                "message": e.msg,
                "Error-Message": "Twilio failed to send Order confirmation SMS",
            }
            return Response(
                data=body,
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            print(f"An error occured: {e}")
            return Response(
                data="An error occured", status=status.HTTP_400_BAD_REQUEST
            )
