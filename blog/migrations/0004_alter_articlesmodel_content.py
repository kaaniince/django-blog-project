# Generated by Django 4.1.7 on 2023-02-18 12:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articlesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
