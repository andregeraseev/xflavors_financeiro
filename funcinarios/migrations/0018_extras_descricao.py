# Generated by Django 4.1.2 on 2022-10-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcinarios', '0017_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='descricao',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
