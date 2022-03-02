# Generated by Django 4.0.2 on 2022-02-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0003_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('A', 'Advanture'), ('C', 'Comedy'), ('Cr', 'Crime'), ('H', 'Historical'), ('F', 'Fantasy'), ('Ho', 'Horror'), ('R', 'Romance'), ('O', 'Other')], max_length=2),
        ),
    ]