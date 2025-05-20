from rest_framework import viewsets
from Ingressos.models  import Cliente, Filme, Checkout, Ingresso
from Ingressos.serializers import ClienteSerializer, FilmeSerializer, CheckoutSerializer, IngressoSerializer
from Ingressos.filters import ClientFilter, FilmeFilter, CheckoutFilmeFilter, IngressoFilter, CheckoutFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message":"Apenas usuários autenticados podem acessar esta view"})

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilmeFilter
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Apenas usuários autenticados podem acessar esta view"})

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CheckoutFilter
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Apenas usuários autenticados podem acessar esta view"})

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngressoFilter
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Apenas usuários autenticados podem acessar esta view"})
