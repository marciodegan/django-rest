from django.shortcuts import render

from .models import DadosPessoais, Customers
from .serializer import DadosPessoaisSerializer, CustomersSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def portfolio_exibir(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}

    return render(request, 'portfolio/portfolio_exibir.html', context)


class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)


class PortfolioView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)


class CustomersListView(APIView):
    serializer_class = CustomersSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Customers.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)


class CustomersView(APIView):
    serializer_class = CustomersSerializer

    def get(self, request, pk, format=None):
        customer = Customers.objects.get(pk=pk)
        serializer = CustomersSerializer(customer)
        return Response(serializer.data)