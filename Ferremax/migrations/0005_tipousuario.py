# Generated by Django 4.2.6 on 2024-06-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferremax', '0004_pedido_idorden_pedido_idsesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('idTipoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTipoUsuario', models.CharField(max_length=20)),
            ],
        ),
    ]
