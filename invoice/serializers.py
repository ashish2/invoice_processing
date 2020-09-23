from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *
from basemodel.views import UserViewSet
from customer.views import CustomerViewSet
from customer.models import Customer

# class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
class InvoiceSerializer(serializers.ModelSerializer):
    # customer = serializers.HyperlinkedRelatedField(
    #     view_name='customer-detail', 
    #     lookup_field='customer', 
    #     queryset=Customer.objects.all()
    #     # source='customer'
    # )

    class Meta:
        model = Invoice
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'

        
class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        # fields = ['url', 'name']
        fields = '__all__'


class PurchaserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchaser
        fields = '__all__'


class InvoiceDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = '__all__'


class LineItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LineItems
        fields = '__all__'


class Invoice_OtherStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice_OtherStatus
        fields = '__all__'
