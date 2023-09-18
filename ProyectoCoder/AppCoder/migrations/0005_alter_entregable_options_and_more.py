# Generated by Django 4.2.4 on 2023-09-18 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_entregable_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entregable',
            options={'ordering': ('nombre', '-fechaDeEntrega', '-entregado'), 'verbose_name': 'Entregable', 'verbose_name_plural': 'Entregables'},
        ),
        migrations.AlterUniqueTogether(
            name='entregable',
            unique_together={('nombre', 'fechaDeEntrega', 'entregado')},
        ),
    ]
