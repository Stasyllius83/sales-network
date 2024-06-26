# Generated by Django 5.0.4 on 2024-05-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='create_data',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='задолженность перед поставщиком'),
        ),
        migrations.AlterField(
            model_name='link',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='link',
            name='house',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='номер дома'),
        ),
        migrations.AlterField(
            model_name='link',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='network.product', verbose_name='продукты'),
        ),
        migrations.AlterField(
            model_name='link',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='улица'),
        ),
    ]
