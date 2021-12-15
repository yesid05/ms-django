from cliente.view.agendarSillaView import AgendarSillaView
from cliente.view.rutaView import RutaView
from cliente.view.sillaView import SillaView

from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
#router.register(r'agendar-silla', AgendarSillaView.as_view())
router.register(r'ruta', RutaView)
router.register(r'silla',SillaView)

urlpatterns = [
    path('agendar-silla/', AgendarSillaView.as_view()),
]

urlpatterns += router.urls
