# Generated by Django 2.0.10 on 2019-01-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
