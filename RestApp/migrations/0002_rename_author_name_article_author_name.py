# Generated by Django 5.0.6 on 2024-06-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Author_name',
            new_name='author_name',
        ),
    ]