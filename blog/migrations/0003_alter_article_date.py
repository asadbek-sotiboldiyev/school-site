# Generated by Django 3.2 on 2023-11-12 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 20, 33, 42, 62980)),
        ),
    ]
