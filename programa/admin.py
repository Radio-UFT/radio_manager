from django.contrib import admin
from programa.models import Programa

class ProgramaAdmin(admin.ModelAdmin):
  list_display = ['id', 'nome', 'descricao', 'horario', 'foto']
  search_fields = ['modelo']

admin.site.register(Programa, ProgramaAdmin)
