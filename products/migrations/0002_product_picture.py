# Generated by Django 4.0.3 on 2022-03-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
