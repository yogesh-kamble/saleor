# Generated by Django 2.0.3 on 2018-07-30 16:25

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0065_auto_20180719_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='cost_price',
            field=django_prices.models.MoneyField(blank=True, currency='INR', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price_override',
            field=django_prices.models.MoneyField(blank=True, currency='INR', decimal_places=2, max_digits=12, null=True),
        ),
    ]
