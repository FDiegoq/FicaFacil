# Generated by Django 5.1.1 on 2024-10-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_tarefa_imagem_tarefa_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='cnpj',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
