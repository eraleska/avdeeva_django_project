# Generated by Django 4.1.1 on 2022-12-12 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_authors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='datenews',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), help_text='Дата публикации'),
        ),
    ]
