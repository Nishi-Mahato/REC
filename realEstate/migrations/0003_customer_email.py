# Generated by Django 2.0.5 on 2020-02-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0002_remove_customer_purchased_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='Null', max_length=200),
        ),
    ]
