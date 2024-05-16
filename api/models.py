

from django.db import models
import uuid

# # Create your models here.
# class UserModel(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField(max_length=100)

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         db_table = 'UserModel'
#         verbose_name = ''
#         verbose_name_plural = ''


# class SchoolModel(models.Model):
#     name = models.CharField(max_length=32)
#     student = models.ForeignKey(UserModel, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.name
#     class Meta:
#         db_table = 'SchoolModel'
#         verbose_name = ''
#         verbose_name_plural = ''

class InvoiceHeaderModel(models.Model):
    id =  uuid.UUID(int=1)
    date= models.DateField(auto_created=True, auto_now_add=True)
    invoiceNumber = models.IntegerField()
    customerName= models.CharField(max_length=42)
    billingAddress = models.CharField(max_length=50)
    shippingAddress = models.CharField(max_length=50)
    gstin= models.CharField(max_length=50)
    totalAmount = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'InvoiceHeaderModel'
        verbose_name = ''
        verbose_name_plural = ''

class InvoiceItemsModel(models.Model):
    id = uuid.UUID(int=1)
    itemName = models.CharField(max_length=32)    
    quantity= models.DecimalField(max_digits=4, decimal_places=2)   
    price= models.DecimalField(max_digits=4, decimal_places=2)
    amount= models.DecimalField(max_digits=4, decimal_places=2)

    
    class Meta:
        db_table = 'InvoiceItemsModel'
        verbose_name = ''
        verbose_name_plural = ''

class InvoiceSundry(models.Model):
    id= uuid.UUID(int=1)    
    billSundryName=models.CharField()   
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'InvoiceSundry'
        verbose_name = ''
        verbose_name_plural = ''