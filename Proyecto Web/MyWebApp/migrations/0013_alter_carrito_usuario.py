# Generated by Django 4.2.1 on 2023-06-19 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebApp', '0012_alter_productos_usuarioprop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyWebApp.usuarioadm', verbose_name='USUARIO'),
        ),
    ]