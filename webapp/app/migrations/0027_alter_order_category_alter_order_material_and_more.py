# Generated by Django 5.0.2 on 2024-03-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_payment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='material',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('รอดำเนินการ', 'รอดำเนินการ'), ('กำลังดำเนินการ', 'กำลังดำเนินการ'), ('ดำเนินการเสร็จสิ้น', 'ดำเนินการเสร็จสิ้น'), ('จัดส่งแล้ว', 'จัดส่งแล้ว'), ('จัดส่งเรียบร้อย', 'จัดส่งเรียบร้อย')], max_length=50),
        ),
    ]