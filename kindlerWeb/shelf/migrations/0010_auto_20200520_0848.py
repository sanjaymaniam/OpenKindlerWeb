# Generated by Django 3.0.6 on 2020-05-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0009_book_exceeded_number_of_clippings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
