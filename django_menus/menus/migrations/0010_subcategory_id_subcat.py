# Generated by Django 4.1.5 on 2023-01-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_generalmenu_id_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='id_subcat',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
