# Generated by Django 5.0.4 on 2024-05-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_link_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='create_data',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='products',
            field=models.ManyToManyField(default=None, to='network.product', verbose_name='продукты'),
        ),
    ]