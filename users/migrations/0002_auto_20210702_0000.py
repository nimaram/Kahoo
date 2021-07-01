# Generated by Django 3.2.4 on 2021-07-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_users_voted'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses_bought',
            field=models.ManyToManyField(blank=True, related_name='cuser', to='courses.Course', verbose_name='دوره های خریداری شده'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('df', 'کاربر عادی'), ('pr', 'کاربر حرفه ای'), ('te', 'معلم'), ('ad', 'ادمین')], default='df', max_length=2, verbose_name='نوع حساب'),
        ),
        migrations.AlterField(
            model_name='user',
            name='wallet_stock',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='موجودی کیف پول'),
        ),
    ]