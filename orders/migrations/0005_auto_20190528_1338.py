# Generated by Django 2.0 on 2019-05-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190528_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_end',
            field=models.DateField(verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_price',
            field=models.IntegerField(verbose_name='单价(元)'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_total_price',
            field=models.IntegerField(verbose_name='总价(元)'),
        ),
    ]
