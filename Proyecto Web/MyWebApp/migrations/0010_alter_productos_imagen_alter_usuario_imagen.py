# Generated by Django 4.2.1 on 2023-06-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebApp', '0009_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='IMAGEN'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='IMAGEN'),
        ),
    ]
