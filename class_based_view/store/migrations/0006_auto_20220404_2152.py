# Generated by Django 3.1.2 on 2022-04-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220403_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='toChika',
        ),
        migrations.RemoveField(
            model_name='books',
            name='toHiro',
        ),
        migrations.AddField(
            model_name='books',
            name='mail',
            field=models.EmailField(default='asdf@mail.com', max_length=254),
        ),
    ]
