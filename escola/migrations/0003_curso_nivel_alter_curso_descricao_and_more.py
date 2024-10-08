# Generated by Django 5.0.3 on 2024-08-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_rename_cursos_curso_rename_estudantes_estudante'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
