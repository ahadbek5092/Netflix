# Generated by Django 4.0.2 on 2022-02-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0011_alter_comment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]