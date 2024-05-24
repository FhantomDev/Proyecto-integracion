from django.urls import path, include
from rest_framework import routers
from .api import ProductoViewSet

from .views import (
    index,
    Nosotros,
    Contacto,
    crud_cuentas,
    crud_productos,
    resultado,
    pedido,
    pago,
    retorno_pago,
    productos,
    Login,
    registro,
    eliminarProducto
)

router = routers.DefaultRouter()
router.register('api/v1/productos', ProductoViewSet, 'productos')

urlpatterns = [
    path("", index, name="index"),
    path("Nosotros", Nosotros, name="Nosotros"),
    path("Contacto", Contacto, name="Contacto"),
    path("crud_cuentas", crud_cuentas, name="crud_cuentas"),
    path("crud_productos", crud_productos, name="crud_productos"),
    path("resultado", resultado, name="resultado"),
    path("pedido", pedido, name="pedido"),
    path("pago", pago, name="pago"),
    path("retorno_pago", retorno_pago, name="retorno_pago"),
    path("productos", productos, name="productos"),
    path("Login", Login, name="Login"),
    path("registro", registro, name="registro"),
    path("eliminarProducto/<str:pk>", eliminarProducto, name="eliminarProducto"),
    path('', include(router.urls))
]
