# Generated by Django 3.2.4 on 2021-06-27 18:08

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='در اینجا میتوانید نام دوره خود را وارد کنید', max_length=130, verbose_name='عنوان دوره')),
                ('slug', models.SlugField(max_length=230, verbose_name='لینک دوره')),
                ('price', models.DecimalField(decimal_places=0, help_text='قیمت محصول رو وارد نمایید', max_digits=10, verbose_name='قیمت محصول')),
                ('body', models.TextField(help_text='در اینجا میتوانید توضیحات مفید در رابطه با پروژه خود اضافه کنید', verbose_name='توضیحات محصول')),
                ('cover', models.ImageField(help_text='در اینجا کاور دوره رو آپلود کنید', upload_to='course_cover/%Y/%m/%d', verbose_name='کاور پروژه')),
                ('cover_video', models.FileField(help_text='در اینجا ویدیو معرفی دوره خود را ببینید', upload_to='course_video/<django.db.models.fields.CharField>', verbose_name='ویدیو معرفی')),
                ('score', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='امتیاز دوره')),
                ('total_score_voted', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=300)),
                ('permission', models.CharField(choices=[('fr', 'رایگان'), ('vp', 'کاربر ویژه'), ('mn', 'نقدی')], help_text='در اینجا سطح دسترسی دوره را تعریف کنید', max_length=8, verbose_name='سطح دسترسی دوره')),
                ('publish_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
                'ordering': ['publish_date', 'score'],
            },
        ),
    ]
