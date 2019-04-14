# Generated by Django 2.1.1 on 2019-04-14 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='分组名')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Group')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.PositiveIntegerField(unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮件地址')),
                ('sex', models.CharField(choices=[('男', 'male'), ('女', 'female')], default='female', max_length=32,
                                         verbose_name='性别')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('Profile_photo',
                 models.FileField(default='img/default_handsome.jpg', upload_to='store/upload/%Y/%m/%d',
                                  verbose_name='头像')),
                ('auth', models.CharField(choices=[('admin', '管理员'), ('user', '用户')], default='user', max_length=128,
                                          verbose_name='权限')),
                ('school', models.CharField(default='未知', max_length=256, verbose_name='学院')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('name', 'student_id')},
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='login.Membership', to='login.User'),
        ),
    ]
