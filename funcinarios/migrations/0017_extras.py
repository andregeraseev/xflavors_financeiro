# Generated by Django 4.1.2 on 2022-10-26 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcinarios', '0016_alter_pagamento_bonus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_extra', models.DateField()),
                ('pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funcinarios.pagamento')),
            ],
        ),
    ]
