# Generated by Django 3.2.5 on 2023-08-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0004_alter_hobby_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]