import cloudinary.models
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=60, unique=True)),
                ('year_published', models.CharField(blank=True, max_length=4)),
                ('synopsis', models.TextField(blank=True)),
                ('cover_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('members_rating', models.PositiveSmallIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_shortlisted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='blog.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('meetup_date', models.DateField()),
                ('details', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Scheduled'), (1, 'Finished'), (2, 'Cancelled')], default=0)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('book1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='meetups', to='blog.book')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-meetup_date'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('meetup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.meetup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]