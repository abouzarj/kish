from rest_framework import fields, serializers
from myapp.models import Customer, ServiceOrder
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id', 'name','phone', 'address']



class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = ['id','customer_id', 'date']
