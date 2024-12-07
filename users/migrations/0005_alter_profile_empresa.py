# Generated by Django 5.1.1 on 2024-12-07 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_tarefa_data_conclusao'),
        ('users', '0004_alter_profile_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.empresa'),
        ),
    ]
