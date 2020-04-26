# Generated by Django 3.0.5 on 2020-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adusert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aduid', models.CharField(max_length=20)),
                ('aduname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'adusert',
            },
        ),
    ]
