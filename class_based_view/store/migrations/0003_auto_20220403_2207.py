# Generated by Django 3.1.2 on 2022-04-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='toChika',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='toHiro',
            field=models.BooleanField(default=False),
        ),
    ]