# Generated by Django 3.2.12 on 2022-02-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20220208_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=0, verbose_name='позиция'),
        ),
    ]
