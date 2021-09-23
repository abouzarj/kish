from django.db.models.query import QuerySet
from myapp.models import Customer, ServiceOrder
from myapp.serializers import CustomerSerializer, ServiceOrderSerializer
from rest_framework import generics

class CustomerList(generics.ListCreateAPIView):
    """
    List all customers, or create a new snippet.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ServiceOrderList(generics.ListCreateAPIView):
    """
    list all orders, or create a new order
    """
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer


class ServiceOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an order.
    """
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer
