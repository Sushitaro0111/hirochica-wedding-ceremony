# Generated by Django 3.1.2 on 2022-04-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20220404_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='picture/', verbose_name='イメージ画像'),
        ),
    ]
