# Generated by Django 4.2.1 on 2023-06-02 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebApp', '0003_remove_usuario_comuna_delete_comuna'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
