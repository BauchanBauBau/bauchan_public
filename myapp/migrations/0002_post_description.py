# Generated by Django 3.1.7 on 2021-05-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=0, max_length=100, verbose_name='概要'),
            preserve_default=False,
        ),
    ]