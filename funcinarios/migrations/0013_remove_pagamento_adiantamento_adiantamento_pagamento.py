# Generated by Django 4.1.2 on 2022-10-25 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcinarios', '0012_alter_adiantamento_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagamento',
            name='adiantamento',
        ),
        migrations.AddField(
            model_name='adiantamento',
            name='pagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funcinarios.pagamento'),
        ),
    ]
