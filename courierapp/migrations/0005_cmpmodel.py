# Generated by Django 3.0.8 on 2020-10-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierapp', '0004_auto_20201020_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='cmpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Context', models.CharField(max_length=500)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
            ],
        ),
    ]
