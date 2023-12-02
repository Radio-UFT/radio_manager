from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from programa.forms import FormularioPrograma
from programa.models import Programa
from radio_manager.biblioteca import LoginObrigatorio
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

class ListarProgramas(LoginObrigatorio, ListView):
  """
  View para listar os programas cadastrados  
  """
  model = Programa
  context_object_name = 'programas'
  template_name = 'programa/listar.html'

  # def get_queryset(self, **kwargs):
  #   pesquisa = self.request.GET.get('pesquisa', None)
  #   queryset = Programa.objects.all()
  #   if pesquisa is not None:
  #     queryset = queryset.filter(modelo__icontains=pesquisa)
  #   return queryset

class CriarProgramas(LoginObrigatorio, CreateView):
  """
  View para a criação de novos veículos.
  """
  model = Programa
  form_class = FormularioPrograma
  template_name = 'programa/novo.html'
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