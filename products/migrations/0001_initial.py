# Generated by Django 3.2.20 on 2023-08-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(default='', max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('shoe_size', models.CharField(blank=True, choices=[('32-34', '32-34'), ('35-36', '35-36'), ('38-40', '38-40'), ('41-43', '41-43'), ('44-46', '44-46')], max_length=10)),
                ('clothes_size', models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2)),
                ('carbon_fp', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('carbon_saved', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('feature_product', models.BooleanField(blank=True, default=False)),
                ('is_sale', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
