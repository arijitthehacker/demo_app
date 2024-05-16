from rest_framework import serializers
from .models import InvoiceHeaderModel, InvoiceSundry, InvoiceItemsModel

class InvoiceHeaderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceHeaderModel
        fields = '__all__'


class InvoiceSundryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceSundry
        fields = '__all__'


class InvoiceItemsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceItemsModel
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = UserModel
#         fields = '__all__'

# class SchoolSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = SchoolModel
#         fields = '__all__'