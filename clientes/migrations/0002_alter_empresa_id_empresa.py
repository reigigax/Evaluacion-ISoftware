# Generated by Django 4.1.2 on 2024-06-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='id_empresa',
            field=models.AutoField(db_column='id_empresa', primary_key=True, serialize=False),
        ),
    ]