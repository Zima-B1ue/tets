# Generated by Django 4.1.7 on 2023-03-16 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='Post',
        ),
    ]
