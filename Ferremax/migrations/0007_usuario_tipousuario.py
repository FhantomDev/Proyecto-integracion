# Generated by Django 4.2.6 on 2024-06-25 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ferremax', '0006_empleado_tipousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Ferremax.tipousuario'),
            preserve_default=False,
        ),
    ]
