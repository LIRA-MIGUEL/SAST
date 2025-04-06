from django.urls import path
from miapp.views import (
    home, vista_diagnostico, vista_auditoria, vista_seguimiento, 
    vista_seguridad, vista_rendimiento
)

# Función para generar un error (para pruebas con Sentry u otro sistema de logs)
def trigger_error(request):
    return 1 / 0  # Esto generará un error 500

urlpatterns = [
    path('', home, name='home'),
    path('diagnostico/', vista_diagnostico, name='vista_diagnostico'),
    path('auditoria/', vista_auditoria, name='vista_auditoria'),
    path('seguimiento/', vista_seguimiento, name='vista_seguimiento'),
    path('seguridad/', vista_seguridad, name='vista_seguridad'),
    path('rendimiento/', vista_rendimiento, name='vista_rendimiento'),
    path('sentry-debug/', trigger_error, name='sentry_debug'),
]

