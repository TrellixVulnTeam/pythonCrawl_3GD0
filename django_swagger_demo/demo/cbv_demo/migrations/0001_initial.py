# Generated by Django 2.0.2 on 2018-05-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('phone', models.CharField(max_length=22)),
                ('address', models.CharField(max_length=44)),
            ],
        ),
    ]
