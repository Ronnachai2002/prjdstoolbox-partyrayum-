# Generated by Django 5.0.2 on 2024-02-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='payment_slips'),
        ),
    ]
