# Generated by Django 3.0.5 on 2020-09-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_resolver', '0008_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]