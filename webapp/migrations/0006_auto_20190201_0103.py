# Generated by Django 2.0.10 on 2019-01-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190201_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastebin',
            name='language',
            field=models.CharField(max_length=50),
        ),
    ]