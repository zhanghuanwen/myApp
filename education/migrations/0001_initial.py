# Generated by Django 2.1.1 on 2018-10-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='li',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('edu', models.CharField(max_length=10)),
            ],
        ),
    ]
