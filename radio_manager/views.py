from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View


class Login(View):
  """
  Classe responsável por autenticar usuários
  """

  def get(self, request):
    mensage = {'Mensagem': ''}

    if not request.user.is_authenticated:
      return render(request, 'login.html', mensage)
    else:
      return HttpResponse('Usuário autenticado!')
    
  def post(self, request):

    # A partir de um formulário da página login.html é obtido as credenciais para autenticação.
    usuario = request.POST.get('nome_usuario', None)
    senha = request.POST.get('senha_usuario', None)

    # Verifica se as credenciais fornecidas passam pela autenticação.
    user = authenticate(request, username=usuario, password=senha)
    if user is not None:

      # Verificação da atividade do usuário no sistema.
      if user.is_active:
        login(request, user)
        return HttpResponse('Usuário autenticado com sucesso!')
      return render(request, 'login.html', {"mensagem": "Usuário inativo"})
    
    return render(request, 'login.html', {"mensagem": "Usuário ou senha invalido"})
  
class Logout(View):
  """
  Classe responsável por realizar o Logout da aplicação.
  """

  def get(self, request):
    logout(request)
    return redirect('/')