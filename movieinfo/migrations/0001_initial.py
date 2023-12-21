# Generated by Django 4.2 on 2023-12-20 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=16, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('searchTitle', models.TextField()),
                ('docid', models.CharField(max_length=16, unique=True)),
                ('title', models.TextField()),
                ('plot', models.TextField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('rating', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.actor')),
                ('companies', models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.company')),
                ('directors', models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.director')),
                ('genres', models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestWatchlistMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieinfo.movieinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TestWatchedMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieinfo.movieinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TestLikeMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieinfo.movieinfo')),
            ],
        ),
        migrations.CreateModel(
            name='OneLineCritic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('starpoint', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieinfo.movieinfo')),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='nations',
            field=models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.nation'),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='posters',
            field=models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.poster'),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='vods',
            field=models.ManyToManyField(blank=True, related_name='movieinfo', to='movieinfo.vod'),
        ),
        migrations.CreateModel(
            name='GPTAnalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('num_of_critics', models.IntegerField(blank=True, null=True)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movieinfo.movieinfo')),
            ],
        ),
    ]
