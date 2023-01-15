# Generated by Django 4.1.5 on 2023-01-11 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_remove_good_subcat_remove_orderitem_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField(unique=True)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.category', verbose_name='cat')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.order', verbose_name='order')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.subcategory', verbose_name='subcat')),
            ],
        ),
    ]
