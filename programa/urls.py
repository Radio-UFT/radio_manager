from django.urls import path
from programa.views import ListarProgramas, FotoPrograma, CriarProgramas

urlpatterns = [
  path('', ListarProgramas.as_view(), name='listar-programas'),
  path('novo/', CriarProgramas.as_view(), name='criar-programas'),
  path('fotos/<str:arquivo>', FotoPrograma.as_view(), name='foto-programa')
]