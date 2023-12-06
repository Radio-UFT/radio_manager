from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class LoginObrigatorio(LoginRequiredMixin, View):
  """
  Método login obrigatório
  """
  redirect_field_name = 'redirecionar'
  login_url = '/'