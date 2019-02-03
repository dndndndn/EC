# Generated by Django 2.1.1 on 2018-09-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='姓名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('student_id', models.IntegerField(unique=True, verbose_name='学号')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮件地址')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='女', max_length=32, verbose_name='性别')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('name', 'sex', 'student_id')},
        ),
    ]
