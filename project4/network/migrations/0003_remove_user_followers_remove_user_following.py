# Generated by Django 4.1.4 on 2023-01-04 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_user_followers_user_following_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
    ]