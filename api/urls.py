from django.urls import path 
from .views import InvoiceSundryListView, InvoiceHeaderListView, InvoiceItemsListView

urlpatterns = [
    path('items/<int:pk>', InvoiceItemsListView.as_view()),
    path('invoiceHeader/', InvoiceHeaderListView.as_view()),
    path('invoiceSundry/', InvoiceSundryListView.as_view()),
]
