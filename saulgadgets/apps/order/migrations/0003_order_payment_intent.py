# Generated by Django 4.0.4 on 2022-04-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_orderitems_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
