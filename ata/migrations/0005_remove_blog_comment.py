# Generated by Django 2.2.3 on 2019-07-23 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ata', '0004_remove_blog_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
    ]