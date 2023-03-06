# Generated by Django 4.1.7 on 2023-03-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_servise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servise',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='servise',
            name='title',
        ),
        migrations.AddField(
            model_name='servise',
            name='desc_1',
            field=models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 1'),
        ),
        migrations.AddField(
            model_name='servise',
            name='desc_2',
            field=models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 2'),
        ),
        migrations.AddField(
            model_name='servise',
            name='desc_3',
            field=models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 3'),
        ),
        migrations.AddField(
            model_name='servise',
            name='desc_4',
            field=models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 4'),
        ),
        migrations.AddField(
            model_name='servise',
            name='h_1',
            field=models.CharField(default='text', max_length=50, verbose_name='Текст розділу'),
        ),
        migrations.AddField(
            model_name='servise',
            name='h_5',
            field=models.CharField(default='text', max_length=50, verbose_name='Назва розділу'),
        ),
        migrations.AddField(
            model_name='servise',
            name='title_1',
            field=models.CharField(default='text', max_length=50, verbose_name='Назва послуги 1'),
        ),
        migrations.AddField(
            model_name='servise',
            name='title_2',
            field=models.CharField(default='text', max_length=50, verbose_name='Назва послуги 1'),
        ),
        migrations.AddField(
            model_name='servise',
            name='title_3',
            field=models.CharField(default='text', max_length=50, verbose_name='Назва послуги 2'),
        ),
        migrations.AddField(
            model_name='servise',
            name='title_4',
            field=models.CharField(default='text', max_length=50, verbose_name='Назва послуги 4'),
        ),
    ]