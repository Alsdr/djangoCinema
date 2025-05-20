from rest_framework import serializers

from Ingressos.models import Cliente, Filme, Checkout, Ingresso

class ClienteSerializer(serializers.ModelSerializer):
    idade = serializers.IntegerField(min_value=18, max_value=100)
    class Meta:
        model = Cliente
        fields = ['cliente_id', 'cpf', 'idade', 'nome']

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['filme_id', 'titulo','duracao', 'sessao_id']

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['checkout_id', 'valor', 'filme_id', 'sessao_id']

class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields: ['ingresso_id']
