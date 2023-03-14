# Generated by Django 3.2.10 on 2023-03-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Создан'), ('processing', 'Обрабатывается'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], default='created', max_length=20),
        ),
    ]