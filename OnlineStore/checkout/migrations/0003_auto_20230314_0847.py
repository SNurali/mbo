# Generated by Django 3.2.10 on 2023-03-14 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20230314_0846'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='order',
            name='one_order_one_address',
        ),
        migrations.RemoveConstraint(
            model_name='order',
            name='one_order_one_cart',
        ),
    ]