# Generated by Django 2.2 on 2021-10-27 20:11

import app_news.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='fl_published',
            field=models.BooleanField(default=False, verbose_name='Для главной страницы'),
        ),
        migrations.AlterField(
            model_name='news',
            name='fl_ready_to_publish',
            field=models.BooleanField(verbose_name='Опубликовать в блоге'),
        ),
        migrations.CreateModel(
            name='FileBlogPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=app_news.models.FileBlogPicture.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='app_news.News')),
            ],
        ),
    ]
