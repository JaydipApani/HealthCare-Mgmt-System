# Generated by Django 5.0.3 on 2024-03-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_alter_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='razorpay_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_pay_signature_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
