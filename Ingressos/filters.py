import django_filters
from Ingressos.models import Cliente, Filme, Ingresso, Checkout_Filme, Checkout


class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='exact')
    rg = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Cliente
        fields = ['id', 'name', 'cpf', 'rg']


class FilmeFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    genero = django_filters.CharFilter(lookup_expr='icontains')
    classificacao = django_filters.NumberFilter()
    duracao = django_filters.NumberFilter()

    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'genero', 'classificacao', 'duracao']

class IngressoFilter(django_filters.FilterSet):
    cliente_id = django_filters.ModelChoiceFilter(queryset=Cliente.objects.all())
    filme_id = django_filters.ModelChoiceFilter(queryset=Filme.objects.all())
    data_compra = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Ingresso
        fields = ['id', 'cliente', 'filme', 'data_compra']


class CheckoutFilmeFilter(django_filters.FilterSet):
    filme_id = django_filters.ModelChoiceFilter(queryset=Filme.objects.all())
    preco = django_filters.RangeFilter()
    quantidade = django_filters.RangeFilter()

    class Meta:
        model = Checkout_Filme
        fields = ['id', 'filme', 'preco', 'quantidade']

class CheckoutFilter(django_filters.FilterSet):
    cliente_id = django_filters.ModelChoiceFilter(queryset=Cliente.objects.all())
    data = django_filters.DateFromToRangeFilter()
    total = django_filters.RangeFilter()

    class Meta:
        model = Checkout
        fields = ['id', 'cliente', 'data', 'total']
