# Generated by Django 3.2.5 on 2021-07-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]
