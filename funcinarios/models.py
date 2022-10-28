from django.db import models
from datetime import datetime

data= datetime.now()
mes_atual = data.month

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=14)
    @property
    def total_a_pagar_no_mes(self):
        pagamentos = self.pagamento_set.filter(data_pagamento__month=mes_atual).order_by("-data_pagamento")
        total_a_pagar = sum([float(k.total_pago) for k in pagamentos])
        return total_a_pagar
    total = 5

    @property
    def total_pago(self):
        pagamentos = self.pagamento_set.all().order_by("-data_pagamento")
        total_a_pagar = sum([float(k.total_pago) for k in pagamentos])
        return total_a_pagar

    def __str__(self):
        return self.nome




class Bonus(models.Model):
    data_bonus = models.DateField()
    bonus_mensal = str(800)
    status = models.BooleanField(default=False)


    @property
    def erro_bonus(self):
        valor = sum([int(k.desconto_erros) for k in self.errobonus_set.all()])
        return valor

    @property
    def valor_ajustado(self):
        valor =  (int(self.bonus_mensal) - int(self.erro_bonus))/4
        return valor

    def __str__(self):
        data = f' {self.data_bonus.strftime("%B")}'
        bonus_str = ''.join(str(data))
        return bonus_str




class Pagamento(models.Model):
    salario = models.DecimalField(max_digits= 6, decimal_places=2)
    data_pagamento = models.DateField()
    status = models.BooleanField(default= False)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return f' {self.funcionario} - {self.data_pagamento.day}/{self.data_pagamento.month}/{self.data_pagamento.year}'

    def valor_bonus(self):
        # valor = sum(float(k.bonus_mensal) for k in self.bonus.bonus_mensal)
        try:
            valor = self.bonus.bonus_mensal
        except:
            valor = 0
        return valor


    def erro(self):
        # valor = sum(float(k.erro_bonus) for k in self.bonus_set.all())
        try:
            valor = self.bonus.erro_bonus
        except:
            valor = 0
        return valor

    @property
    def valor_adiantamento(self):
        valor  = sum([float(k.valor) for k in self.adiantamento_set.all()])
        return valor

    @property
    def valor_extra(self):
        valor = sum([float(k.valor) for k in self.extras_set.all()])
        return valor

    @property
    def valor_ajustado(self):
        # valor = sum([float(k.valor_ajustado) for k in self.bonus_set.all()])
        try:
            valor = self.bonus.valor_ajustado
        except:
            valor = 0
        return valor

    def valor_a_pagar(self):
        valor = float(self.valor_extra ) +float(self.salario )+ float(self.valor_ajustado) - float(self.valor_adiantamento)
        return valor

    @property
    def total_pago(self):
        valor = float(self.valor_extra ) +float(self.salario ) + float(self.valor_ajustado)
        return valor

class Adiantamento(models.Model):
    valor = models.DecimalField(max_digits= 6, decimal_places=2, blank=True, null=True)
    data_adiantamento = models.DateField(auto_created=True)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.valor)
    # def pagar(self):
    #     adiantamentos = Adiantamento.objects.filter(pagamento_id=self.id)
    #     print(adiantamentos)
    #     total = 0
    #     for adiantamento in adiantamentos:
    #         total += adiantamento.valor
    #
    #         print(adiantamento)
    #         print(adiantamento.valor)
    #         print(total)
    #     return total

    def soma(self):

        total = self.pagamento.salario - self.valor
        return total






class ErroBonus(models.Model):
    bonus_erro = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=True)
    numero_pedido = models.IntegerField()
    desconto_erros = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    data_erro = models.DateField(auto_created=True)

    def __str__(self):
        return str(self.numero_pedido)




class Ferias(models.Model):
    data_inicio= models.DateField()
    data_fim = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True)

    @property
    def tempo_de_ferias(self):
        duracao = self.data_fim -self.data_inicio
        return duracao.days
    def __str__(self):
        return str(self.data_inicio)


class Extras(models.Model):
    valor = models.DecimalField(max_digits= 6, decimal_places=2)
    descricao = models.CharField(max_length= 300, null=True, blank=True)
    data_extra = models.DateField()
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.pagamento)



