# Generated by Django 4.0.1 on 2022-01-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_persona_idnumber_alter_persona_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='isStaff',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
