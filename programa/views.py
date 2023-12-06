from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from programa.forms import FormularioPrograma
from programa.models import Programa
from radio_manager.biblioteca import LoginObrigatorio
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListAPIView
from programa.serializers import SerializadorPrograma
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import permissions

class ListarProgramas(LoginObrigatorio, ListView):
  """
  View para listar os programas cadastrados  
  """
  model = Programa
  context_object_name = 'programas'
  template_name = 'programa/listar.html'

class CriarProgramas(LoginObrigatorio, CreateView):
  """
  View para a criação de novos programas.
  """
  model = Programa
  form_class = FormularioPrograma
  template_name = 'programa/novo.html'
  success_url = reverse_lazy('listar-programas')

class EditarProgramas(LoginObrigatorio, UpdateView):
  """
  View para a edição de programas já cadastrados.
  """
  model = Programa
  form_class = FormularioPrograma
  template_name = 'programa/editar.html'
  success_url = reverse_lazy('listar-programas')

class DeletarProgramas(LoginObrigatorio, DeleteView):
  """
  View para a exclusão de programas.
  """
  model = Programa
  template_name = 'programa/deletar.html'
  success_url = reverse_lazy('listar-programas')
  
class FotoPrograma(LoginObrigatorio):
  """
  View para retornar a foto dos programas
  """
  def get(self, request, arquivo):
    try:
      programa = Programa.objects.get(foto=f'programa/fotos/{arquivo}')
      return FileResponse(programa.foto)
    except ObjectDoesNotExist:
      raise Http404("Foto não encontrada ou acesso não autorizado")
    except Exception as exception:
      raise exception
    
class APIListarProgramas(ListAPIView):    
  """
  View para listar instâncias do programa (utilizando da API REST)    
  """
  serializer_class = SerializadorPrograma  
  def get_queryset(self):        
    return Programa.objects.all()
