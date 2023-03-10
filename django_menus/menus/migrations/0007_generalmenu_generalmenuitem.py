# Generated by Django 4.1.5 on 2023-01-11 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_remove_orderitem_cat_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generalmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField(unique=True)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.category', verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralmenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.category', verbose_name='cat')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.generalmenu', verbose_name='Generalmenu')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.subcategory', verbose_name='subcat')),
            ],
        ),
    ]
