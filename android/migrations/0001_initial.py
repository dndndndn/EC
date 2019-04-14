# Generated by Django 2.1.1 on 2019-04-14 07:28

import django.db.models.deletion
from django.db import migrations, models

import android.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Bool', models.BooleanField(default=False, verbose_name='正确标志')),
                ('type',
                 models.CharField(choices=[('txt', 'text'), ('img', 'image')], max_length=10, verbose_name='类型')),
                ('text', models.TextField(blank=True, null=True, verbose_name='文字')),
                ('img', models.FileField(blank=True, null=True, upload_to=android.models.upload_chioce)),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('m_time', models.DateTimeField(auto_now=True, verbose_name='最新修改日期')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                related_name='choice_creater', to='login.User', verbose_name='创建人')),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
                'ordering': ['-ID'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceTips',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('txt', 'text'), ('img', 'image'), ('null', 'null')], max_length=10,
                                          verbose_name='类型')),
                ('text', models.TextField(blank=True, null=True, verbose_name='文字')),
                ('img', models.FileField(blank=True, null=True, upload_to=android.models.upload_chioce_Tips)),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('m_time', models.DateTimeField(auto_now=True, verbose_name='最新修改日期')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                related_name='choiceTips_creater', to='login.User',
                                                verbose_name='创建人')),
                ('related_choice',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='choiceTips',
                                      to='android.Choice', verbose_name='所属选项')),
            ],
            options={
                'verbose_name': '错误选项提示',
                'verbose_name_plural': '错误选项提示',
                'ordering': ['-ID'],
            },
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='事件名称')),
                ('event_type', models.SmallIntegerField(
                    choices=[(0, '其它'), (1, '添加/删除问题'), (2, '编辑问题'), (3, '问题管理'), (4, '添加测试'), (5, '定期维护'),
                             (6, '用户管理添加\\删除'), (7, '用户管理更新')], default=5, verbose_name='事件类型')),
                ('component', models.CharField(blank=True, max_length=256, null=True, verbose_name='事件子项')),
                ('detail', models.TextField(verbose_name='事件详情')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='事件时间')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '事件纪录',
                'verbose_name_plural': '事件纪录',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Q_Status', models.SmallIntegerField(choices=[(0, '在线'), (1, '下线'), (2, '审核'), (3, '编辑')], default=2,
                                                      verbose_name='状态')),
                ('text', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='题目标题')),
                ('choice_type',
                 models.SmallIntegerField(choices=[(0, '单选'), (1, '多选'), (2, '拍照'), (3, '填空')], verbose_name='选项类型')),
                ('choice_length', models.SmallIntegerField(verbose_name='选项长度')),
                ('url', models.CharField(max_length=256, verbose_name='url')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('m_time', models.DateTimeField(auto_now=True, verbose_name='最新修改日期')),
                ('AC', models.PositiveIntegerField(default=0, verbose_name='全对人数')),
                ('general_priority',
                 models.SmallIntegerField(choices=[(0, '难'), (1, '较难'), (2, '适中'), (3, '较易'), (4, '易')],
                                          verbose_name='优先度')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                related_name='question_creater', to='login.User', verbose_name='创建人')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题目',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='分组名')),
                ('c_day', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                related_name='Group_creater', to='login.User', verbose_name='创建人')),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组',
            },
        ),
        migrations.CreateModel(
            name='QuestionMembership',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='分组名')),
                ('c_day', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('tips', models.CharField(max_length=25, verbose_name='备注')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='android.QuestionGroup')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='android.Question')),
            ],
            options={
                'verbose_name': '分组关系表',
                'verbose_name_plural': '分组关系表',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('AC', models.BooleanField(default=False)),
                ('end_time', models.DateTimeField(auto_now_add=True, verbose_name='完成日期')),
                ('duration', models.DurationField()),
                ('related_question',
                 models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                      related_name='r_question', to='android.Question', verbose_name='所属问题')),
            ],
            options={
                'verbose_name': '记录',
                'verbose_name_plural': '记录',
                'ordering': ['-ID'],
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type',
                 models.CharField(choices=[('txt', 'text'), ('img', 'image')], max_length=15, verbose_name='题干类型')),
                ('img', models.FileField(blank=True, upload_to=android.models.upload_solution)),
                ('text', models.TextField(blank=True)),
                ('next_content',
                 models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                      to='android.Solution')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               related_name='so_qu', to='android.Question', verbose_name='创建人')),
            ],
        ),
        migrations.CreateModel(
            name='statisic',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type',
                 models.CharField(choices=[('txt', 'text'), ('img', 'image')], max_length=15, verbose_name='题干类型')),
                ('img', models.FileField(blank=True, upload_to=android.models.upload_stem)),
                ('text', models.TextField(blank=True)),
                ('next_content',
                 models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                      to='android.Stem')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               related_name='st_qu', to='android.Question', verbose_name='创建人')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签名')),
                ('c_day', models.DateField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(blank=True, to='android.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='r_user', to='login.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='members',
            field=models.ManyToManyField(through='android.QuestionMembership', to='android.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='solution',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='question_solution', to='android.Solution'),
        ),
        migrations.AddField(
            model_name='question',
            name='stem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='question_stem', to='android.Stem'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='android.Tag', verbose_name='知识点标签'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='quesion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='android.Question'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='android.Record'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='target_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='target_user', to='login.User', verbose_name='目标用户'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='execute_user', to='login.User', verbose_name='事件执行人'),
        ),
        migrations.AddField(
            model_name='choice',
            name='related_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='choice', to='android.Question', verbose_name='所属问题'),
        ),
        migrations.AddField(
            model_name='choice',
            name='tags',
            field=models.ManyToManyField(blank=True, to='android.Tag', verbose_name='标签'),
        ),
    ]
