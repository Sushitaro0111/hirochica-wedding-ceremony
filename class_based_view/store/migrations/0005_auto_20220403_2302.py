# Generated by Django 3.1.2 on 2022-04-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_books_price2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='price2',
        ),
        migrations.AddField(
            model_name='books',
            name='type_name',
            field=models.TextField(choices=[(1, '新郎'), (2, '新婦'), (3, '両方')], default='新郎', verbose_name='宛先'),
        ),
    ]
