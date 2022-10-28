from django.db import models
from funcinarios.models import Pagamento
from datetime import datetime
data = datetime.now()
mes_atual = data.month



class Depositos(models.Model):
    data= models.DateField()
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Geral(models.Model):

    data = models.DateField(null=True)
    valor_bruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    @property
    def mes_atual(self):
        return self.data.month

    @property
    def nome(self):
        mes =self.data.strftime("%B/%y")

        return mes


    @property
    def total_funcionario_mes(self):
        funcionarios = Pagamento.objects.filter(data_pagamento__month=self.mes_atual)
        return sum([(funcionario.total_pago) for funcionario in funcionarios])


    @property
    def total_depositos(self):
        depositos = Depositos.objects.filter(data__month=self.mes_atual).order_by("-data")
        return sum([(deposito.valor) for deposito in depositos])


    @property
    def total(self):
        return round(float(self.total_depositos) + float(self.total_funcionario_mes),2)

    @property
    def total_liquido(self):
        if self.valor_bruto:
            return round(float(self.valor_bruto) - float(self.total),2)
        else:
            return "valor a calcular"
