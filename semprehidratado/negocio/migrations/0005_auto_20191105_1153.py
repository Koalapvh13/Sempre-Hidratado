# Generated by Django 2.2.4 on 2019-11-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0004_auto_20191105_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Entrega'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
