# Generated by Django 4.2.6 on 2023-10-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_notebooks_televisores'),
    ]

    operations = [
        migrations.AddField(
            model_name='celulares',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='celulares',
            name='modelo',
            field=models.CharField(max_length=30),
        ),
    ]
