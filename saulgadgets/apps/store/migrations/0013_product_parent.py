# Generated by Django 4.0.4 on 2022-05-18 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_num_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.product'),
        ),
    ]
