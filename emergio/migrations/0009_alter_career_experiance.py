# Generated by Django 5.0.3 on 2024-04-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergio', '0008_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='experiance',
            field=models.CharField(max_length=20),
        ),
    ]
