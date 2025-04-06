import logging
import time
import sentry_sdk
from django.http import HttpResponse, HttpResponseNotFound

# Obtener loggers para diferentes propósitos
logger_diag = logging.getLogger('diagnostico')
logger_auditoria = logging.getLogger('auditoria')
logger_seguimiento = logging.getLogger('seguimiento')
logger_seguridad = logging.getLogger('seguridad')
logger_rendimiento = logging.getLogger('rendimiento')

def home(request):
    return HttpResponse("<h1 style='color: #007bff; text-align: center;'>Bienvenido al Sistema de Registro de Eventos</h1>")

def vista_diagnostico(request):
    logger_diag.debug("Se realizó un análisis del sistema en busca de errores potenciales.")
    sentry_sdk.capture_message("Diagnóstico ejecutado", level="debug")
    return HttpResponse("<h1 style='color: #28a745;'>Diagnóstico Completado</h1><p>Se han registrado los detalles en <strong>logs/diagnostico.log</strong>.</p>")

def vista_auditoria(request):
    usuario = request.user if request.user.is_authenticated else "Usuario anónimo"
    mensaje = f"Registro de auditoría: {usuario} accedió al sistema."
    logger_auditoria.info(mensaje)
    sentry_sdk.capture_message(mensaje, level="info")
    return HttpResponse("<h1 style='color: #17a2b8;'>Auditoría Registrada</h1><p>Tu acceso ha sido almacenado para futuras referencias.</p>")

def vista_seguimiento(request):
    usuario = request.user if request.user.is_authenticated else "Usuario desconocido"
    mensaje = f"Seguimiento: {usuario} visitó la URL {request.path}"
    logger_seguimiento.info(mensaje)
    sentry_sdk.capture_message(mensaje, level="info")
    return HttpResponse("<h1 style='color: #ffc107;'>Seguimiento de Actividad</h1><p>Se ha registrado la actividad del usuario en el sistema.</p>")

def vista_seguridad(request):
    ip_usuario = request.META.get('REMOTE_ADDR', 'Dirección IP no identificada')
    mensaje = f"Posible intento de acceso sospechoso desde {ip_usuario}."
    logger_seguridad.warning(mensaje)
    sentry_sdk.capture_message(mensaje, level="warning")
    return HttpResponse("<h1 style='color: #dc3545;'>Alerta de Seguridad</h1><p>Se detectó un posible intento de acceso sospechoso.</p>")

def vista_rendimiento(request):
    start_time = time.time()
    time.sleep(1)  # Simulación de procesamiento
    end_time = time.time()
    execution_time = end_time - start_time
    mensaje = f"Tiempo de ejecución: {execution_time:.2f} segundos"
    logger_rendimiento.info(mensaje)
    sentry_sdk.capture_message(mensaje, level="info")
    return HttpResponse(f"<h1 style='color: #6c757d;'>Análisis de Rendimiento</h1><p>Tiempo de procesamiento: <strong>{execution_time:.2f} segundos</strong>.</p>")

def error_404_view(request, exception):
    mensaje = f"Error 404 - Página No Encontrada: {request.path}"
    sentry_sdk.capture_message(mensaje, level="error")
    return HttpResponseNotFound("""
        <h1 style='color: red; text-align: center;'>⚠️ Error 404 - Página No Encontrada</h1>
        <p style='text-align: center;'>Lo sentimos, la página que buscas no existe.</p>
        <p style='text-align: center;'><a href='/' style='color: #007bff; text-decoration: none;'>🔙 Volver al inicio</a></p>
    """)

# Función de prueba para generar un error
def trigger_error(request):
    try:
        return 1 / 0  # Esto generará un error 500
    except Exception as e:
        sentry_sdk.capture_exception(e)  # Captura el error en Sentry
        logger_rendimiento.error(f"Error detectado: {e}")
        return HttpResponse("<h1 style='color: red;'>Error generado intencionalmente</h1>", status=500)
