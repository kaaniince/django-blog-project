# Generated by Django 4.1.7 on 2023-02-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]