# Generated by Django 4.0.2 on 2022-02-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0012_rename_movie_id_comment_movie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Advanture', 'Advanture'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Historical', 'Historical'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Other', 'Other')], max_length=15),
        ),
    ]
