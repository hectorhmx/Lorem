# Generated by Django 2.0.5 on 2018-05-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0002_auto_20180512_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degrees',
            old_name='url',
            new_name='link',
        ),
        migrations.AlterField(
            model_name='degrees',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ImgPlanes', verbose_name='Imagen'),
        ),
    ]
