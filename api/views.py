from django.shortcuts import render

# Create your views here.
from .models import InvoiceHeaderModel, InvoiceSundry, InvoiceItemsModel
from rest_framework import generics

from .serializers import InvoiceHeaderModelSerializer, InvoiceItemsModelSerializer, InvoiceSundryModelSerializer

class InvoiceItemsListView(generics.ListCreateAPIView):
    queryset = InvoiceItemsModel.objects.all()
    serializer_class = InvoiceItemsModelSerializer

class InvoiceHeaderListView(generics.ListCreateAPIView):
    queryset = InvoiceHeaderModel.objects.all()
    serializer_class = InvoiceHeaderModelSerializer


class InvoiceSundryListView(generics.ListCreateAPIView):
    queryset = InvoiceSundry.objects.all()
    serializer_class = InvoiceSundryModelSerializer

