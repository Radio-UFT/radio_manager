from django.urls import path
from programa.views import ListarProgramas, FotoPrograma, CriarProgramas, EditarProgramas, DeletarProgramas, APIListarProgramas

urlpatterns = [
  path('', ListarProgramas.as_view(), name='listar-programas'),
  path('novo/', CriarProgramas.as_view(), name='criar-programas'),
  path('<int:pk>/', EditarProgramas.as_view(), name='editar-programas'),
  path('deletar/<int:pk>/', DeletarProgramas.as_view(), name='deletar-programas'),
  path('fotos/<str:arquivo>', FotoPrograma.as_view(), name='foto-programa'),
  
  # API path

  path('api/', APIListarProgramas.as_view(), name='api-listar-programas'),
]