from rest_framework import serializers
from programa.models import Programa
from drf_extra_fields.fields import Base64ImageField

class SerializadorPrograma(serializers.ModelSerializer):
  foto_base64 = Base64ImageField(required=False, represent_in_base64=True)

  class Meta:
      model = Programa
      exclude = []

  def top_representation(self, instance):
    representation = super().to_representation(instance)
    representation['horario'] = instance.horario.strftime('%H:%M:%S')  # Formatando o horário como string
    return representation
