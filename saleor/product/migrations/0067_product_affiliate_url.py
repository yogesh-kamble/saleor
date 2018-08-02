# Generated by Django 2.0.3 on 2018-08-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0066_auto_20180730_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='affiliate_url',
            field=models.URLField(blank=True, default=None, help_text='Insert the Affiliate Product Url which will replace Add to Cart button with Affiliate Url Click', null=True),
        ),
    ]