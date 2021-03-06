# Generated by Django 3.2.5 on 2021-07-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=256)),
                ('release_year', models.PositiveIntegerField(verbose_name='Release Year')),
                ('author', models.ManyToManyField(to='authors.Author')),
            ],
        ),
    ]
