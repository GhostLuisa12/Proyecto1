# Generated by Django 4.0.1 on 2022-01-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=120)),
                ('phone', models.IntegerField(max_length=10)),
                ('idNumber', models.IntegerField(max_length=100)),
                ('isStaff', models.BooleanField()),
                ('picture', models.ImageField(upload_to='pictures/')),
            ],
        ),
    ]
