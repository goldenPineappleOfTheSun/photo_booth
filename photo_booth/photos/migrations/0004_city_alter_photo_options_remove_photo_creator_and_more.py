# Generated by Django 4.0.4 on 2022-08-05 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0003_remove_photo_photo_url_alter_photo_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(db_index=True, max_length=20, verbose_name='Город')),
                ('operators', models.ManyToManyField(related_name='cities', to=settings.AUTH_USER_MODEL, verbose_name='Оператор')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['city_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='display',
        ),
        migrations.AddField(
            model_name='photo',
            name='page_in_journal',
            field=models.IntegerField(default=0, verbose_name='Номер страницы в журнале'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_image',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='photo',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_name',
            field=models.CharField(default='', max_length=20, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('journal_name', models.CharField(default='', max_length=20, null=True, verbose_name='Название журнала')),
                ('total_pages', models.IntegerField(default=33, null=True, verbose_name='Всего страниц')),
                ('filled_pages', models.IntegerField(default=0, null=True, verbose_name='Заполнено страниц')),
                ('journal_city', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='photos.city', verbose_name='Город')),
                ('journal_owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Оператор')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='journal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='photos.journal', verbose_name='Журнал'),
        ),
    ]
