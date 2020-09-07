# Generated by Django 2.1.7 on 2020-05-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_resolver', '0004_auto_20200514_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisasterInfo',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('longtitude', models.FloatField(max_length=100)),
                ('latitude', models.FloatField(max_length=100)),
                ('depth', models.FloatField(max_length=100)),
                ('magnitude', models.FloatField(max_length=100)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LandslideRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MasonryStructure',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MissingStatics',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('number', models.IntegerField()),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
    ]