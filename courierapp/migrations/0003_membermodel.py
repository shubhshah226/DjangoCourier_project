# Generated by Django 3.0.8 on 2020-10-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierapp', '0002_backendmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=120)),
                ('LastName', models.CharField(max_length=120)),
                ('PhoneNumber', models.IntegerField()),
                ('Email', models.CharField(max_length=120)),
            ],
        ),
    ]