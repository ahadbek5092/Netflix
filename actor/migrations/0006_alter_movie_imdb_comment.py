# Generated by Django 4.0.2 on 2022-02-24 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actor', '0005_movie_actors_delete_movie_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.CharField(max_length=3),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='actor.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
