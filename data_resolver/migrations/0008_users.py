# Generated by Django 3.0.5 on 2020-09-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_resolver', '0007_auto_20200602_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('usname', models.CharField(max_length=100)),
                ('pswd', models.CharField(max_length=100)),
            ],
        ),
    ]
