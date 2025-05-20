from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Ingressos.views import ClienteViewSet, IngressoViewSet, FilmeViewSet, CheckoutViewSet

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('filmes', FilmeViewSet)
router.register('ingressos', IngressoViewSet)
router.register('checkout', CheckoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]