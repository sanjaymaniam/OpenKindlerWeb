# Generated by Django 3.0.6 on 2020-05-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20200519_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clipping',
            name='author',
        ),
        migrations.RemoveField(
            model_name='clipping',
            name='title',
        ),
        migrations.AlterField(
            model_name='clipping',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shelf.Book'),
        ),
    ]
