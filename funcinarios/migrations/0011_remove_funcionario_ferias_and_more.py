# Generated by Django 4.1.2 on 2022-10-25 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcinarios', '0010_remove_adiantamento_pagamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='ferias',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='pagamento',
        ),
        migrations.AddField(
            model_name='ferias',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funcinarios.funcionario'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funcinarios.funcionario'),
        ),
    ]
