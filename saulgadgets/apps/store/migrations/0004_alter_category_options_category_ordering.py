# Generated by Django 4.0.4 on 2022-04-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_options_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('ordering',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(default=0),
        ),
    ]
