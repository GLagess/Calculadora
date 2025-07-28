from django.db import models
from django.contrib.auth.models import User
class Operacao(models.Model):
    usuario   = models.ForeignKey(User, on_delete=models.CASCADE)
    expressao = models.CharField("Expressão", max_length=50)
    resultado = models.CharField("Resultado", max_length=50)
    data_hora = models.DateTimeField("Data/Hora", auto_now_add=True)

    def __str__(self):
        return f"{self.expressao} = {self.resultado}"
