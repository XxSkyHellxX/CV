# Generated by Django 4.2.1 on 2023-06-17 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebApp', '0010_alter_productos_imagen_alter_usuario_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_producto_carrito', models.AutoField(primary_key=True, serialize=False, verbose_name='CARRITO ID')),
                ('cantidad', models.IntegerField(verbose_name='STOCK SOLICITADO')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyWebApp.productos', verbose_name='PRODUCTO')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyWebApp.usuario', verbose_name='USUARIO')),
            ],
        ),
    ]