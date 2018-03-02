# Generated by Django 2.0.1 on 2018-02-19 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180219_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
