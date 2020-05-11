from rest_framework import serializers
from .models import DadosPessoais, Customers

class DadosPessoaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosPessoais
        depth = 1
        fields = ['id', 'name', 'adress', 'city', 'cep', 'phone', 'mobile']


class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        depth = 1
        fields = ['id', 'first_name', 'last_name', 'gender', 'company', 'city', 'title']