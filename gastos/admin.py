from django.contrib import admin
from gastos.models import Depositos, Geral
from datetime import datetime

data= datetime.now()
mes_admin = data.month

class ListandoDepositos(admin.ModelAdmin):
    list_display = ('id','descricao','valor','data','created_at')
    list_display_links = ('id',)
    list_filter = ('data',)
    search_fields = ['descricao', 'valor',]
    ordering = ('-data',)

admin.site.register(Depositos, ListandoDepositos)


# def mudar_mes(modeladmin, request, queryset, mes = mes_admin):
#     mes_admin = mes + 1
#     return mes_admin




class ListandoGeral(admin.ModelAdmin):
    list_display = ('nome', 'valor_bruto','total', 'total_depositos','total_funcionario_mes','total_liquido')
    # list_display_links = ('id',)

    # actions = [mudar_mes]




admin.site.register(Geral, ListandoGeral)