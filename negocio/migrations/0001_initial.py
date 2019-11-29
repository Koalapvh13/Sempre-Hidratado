# Generated by Django 2.2.4 on 2019-11-03 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50, verbose_name='Nome Dispositivo')),
                ('uuid', models.CharField(max_length=50, verbose_name='Arduino ID')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=25, verbose_name='CNPJ')),
                ('telefone', models.CharField(max_length=30, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False, verbose_name='Estado')),
                ('data_pedido', models.DateTimeField(auto_now=True, verbose_name='Data Solicitação')),
                ('data_entrega', models.DateTimeField(verbose_name='Data Entrega')),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negocio.Dispositivo')),
            ],
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negocio.Empresa'),
        ),
    ]