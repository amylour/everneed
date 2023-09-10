# Generated by Django 3.2.20 on 2023-09-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='clothes_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]