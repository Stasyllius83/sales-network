# Generated by Django 5.0.4 on 2024-05-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_link_create_data_alter_link_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='задолженность перед поставщиком'),
        ),
    ]
