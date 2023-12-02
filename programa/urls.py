from django.urls import path
from programa.views import ListarProgramas, FotoPrograma

urlpatterns = [
  path('', ListarProgramas.as_view(), name='listar-programas'),
  path('fotos/<str:arquivo>', FotoPrograma.as_view(), name='foto-programa')
]