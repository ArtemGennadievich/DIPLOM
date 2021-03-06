# Generated by Django 4.0.5 on 2022-06-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to='car_img/')),
                ('main_title', models.CharField(max_length=200, verbose_name='Название блока')),
                ('maim_date_add', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('maim_date', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Блок_контент',
                'verbose_name_plural': 'Блоки_контента',
            },
        ),
    ]
