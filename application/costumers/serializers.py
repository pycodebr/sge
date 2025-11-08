from rest_framework import serializers
from costumers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'
