from django.contrib import admin
from funcinarios.models import Funcionario,Ferias,Pagamento,ErroBonus,Bonus,Adiantamento,Extras


class ListandoFuncionarios(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','total_a_pagar_no_mes')
    list_display_links = ('id', 'nome',)

admin.site.register(Funcionario, ListandoFuncionarios)

class ListandoFerias(admin.ModelAdmin):
    list_display = ('id','funcionario','data_inicio','data_fim','tempo_de_ferias')
    list_display_links = ('id',)
    list_filter = ('data_inicio', 'funcionario')
admin.site.register(Ferias, ListandoFerias)

class ListandoPagamento(admin.ModelAdmin):
    list_display = ('id','funcionario','salario','data_pagamento','status','valor_bonus','valor_adiantamento','erro','valor_ajustado','valor_extra','valor_a_pagar','total_pago')
    list_display_links = ('id',)
    ordering = ('-data_pagamento',)
    list_filter = ('data_pagamento', 'funcionario','status',)
    list_per_page = 30


    date_hierarchy = 'data_pagamento'
admin.site.register(Pagamento, ListandoPagamento)

class ListandoBonus(admin.ModelAdmin):
    list_display = ('id','data_bonus','bonus_mensal','status','erro_bonus', 'valor_ajustado')
    list_display_links = ('id',)
    list_filter = ('data_bonus', 'status')

admin.site.register(Bonus, ListandoBonus)

class ListandoErroBonus(admin.ModelAdmin):
    list_display = ('id','numero_pedido','desconto_erros','data_erro')
    list_display_links = ('id',)
    list_filter = ('numero_pedido', 'data_erro')

admin.site.register(ErroBonus, ListandoErroBonus)

class ListandoExtra(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'valor', 'data_extra')
    list_display_links = ('id',)

admin.site.register(Extras, ListandoExtra)


