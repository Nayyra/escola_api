# Generated by Django 5.0.3 on 2024-08-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_curso_nivel_alter_curso_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nome',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
