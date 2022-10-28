from datetime import datetime

from django.shortcuts import render
from funcinarios.models import *


def index(request):
    data= datetime.now()
    mes_atual = data.month
    funcionarios = Funcionario.objects.all().order_by("pagamento__data_pagamento")
    pagamentos = Pagamento.objects.filter(data_pagamento__month=mes_atual).order_by("-data_pagamento")

    total_a_pagar = sum([float(k.total_pago) for k in pagamentos])
    print(total_a_pagar)


    # for pagamento in pagamentos:
    #
    #     funcionario_dic = {}
    #
    #     valor_bonus = [int(k.bonus_mensal) for k in pagamento.bonus_set.all()]
    #     bonus = pagamento.bonus_set.all()
    #     valorerro=[]
    #     for erro in bonus:
    #         # erro = erro.errobonus_set.all()
    #         valor_erro =  [int(k.desconto_erros) for k in erro.errobonus_set.all()]
    #         valorerro.append(sum(valor_erro))
    #
    #     # print(pagamento.funcionario, int(pagamento.salario) +  sum(valor_bonus)- sum(valorerro) )
    #     valor_adiantamento = [int(k.valor) for k in pagamento.adiantamento_set.all()]
    #
    #     # print(sum(valor_adiantamento) )
    #
    #
    #     total_a_pagar =  int(pagamento.salario) + sum(valor_bonus) - sum(valorerro) - sum(valor_adiantamento)
    #     # print(pagamento.funcionario, pagamento.salario, valor_bonus, valor_adiantamento, total_a_pagar)
    #     # funcionario_dic.update({"salario": int(pagamentos.salario)})
    #     # funcionario_dic.update({"valor_bonus": valor_bonus})
    #     # funcionario_dic.update({"valor_adiantamento": valor_adiantamento})
    #     # funcionario_dic.update({"total_a_pagar":total_a_pagar})
    #     total.update({(str(pagamento.funcionario) + str(pagamento.id)) : [pagamento.salario, valor_bonus, valor_adiantamento, total_a_pagar]})
    # print(total)
    # # teste = dic_pagamento[funcionario]
    #
    #
    #
    # # pagamento = Pagamento.objects.filter(data_pagamento__month=mes_atual)



    context = {
        "funcionarios" : funcionarios,
        "pagamentos": pagamentos,

    }
    return render(request, 'index.html', context)
