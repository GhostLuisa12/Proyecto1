# Generated by Django 4.0.1 on 2022-01-22 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_persona_isstaff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=30),
        ),
    ]
