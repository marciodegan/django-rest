# Generated by Django 3.0.6 on 2020-05-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('adress', models.CharField(max_length=100, verbose_name='Endereço')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=50, verbose_name='Cep')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('mobile', models.CharField(max_length=20, verbose_name='Celular')),
                ('about', models.TextField(max_length=255, verbose_name='Sobre')),
                ('data_nascimento', models.CharField(default='01 de janeiro de 2000', max_length=255, verbose_name='Data Nascimento')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('conhecimentos', models.TextField(max_length=255, verbose_name='Conhecimentos')),
                ('github', models.CharField(default='http://github.com/SeuGit', max_length=100, verbose_name='Github')),
                ('current_position', models.CharField(max_length=100, verbose_name='Cargo atual')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Dados Pessoais',
                'verbose_name_plural': 'Dados Pessoais',
            },
        ),
    ]
