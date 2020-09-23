from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import *
from .models import *


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer

class InvoiceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer

class LineItemsViewSet(viewsets.ModelViewSet):
    queryset = LineItems.objects.all()
    serializer_class = LineItemsSerializer

class Invoice_OtherStatusViewSet(viewsets.ModelViewSet):
    queryset = Invoice_OtherStatus.objects.all()
    serializer_class = Invoice_OtherStatusSerializer
