# coding=utf-8

from django.db import models

# Create your models here.
from login.models import User


class Question(models.Model):
    question_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '审核'),
        (3, '编辑'),
    )
    choice_type = (
        (0, "单选"),
        (1, "多选"),
        (2, "拍照"),
        (3, "填空"),
    )
    ID = models.AutoField(primary_key=True)
    Q_Status = models.SmallIntegerField(choices=question_status, verbose_name="状态", default=2)
    text = models.CharField(max_length=15, null=True, blank=True, verbose_name="题目标题", default="")
    choice_type = models.SmallIntegerField(choices=choice_type, verbose_name="选项类型")
    choice_length = models.SmallIntegerField(verbose_name="选项长度")
    create_by = models.ForeignKey(User, null=True, blank=True, verbose_name='创建人', related_name="quesion_creater",
                                  on_delete=models.SET_NULL)
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='最新修改日期')
    stem = models.OneToOneField('content', related_name="question_stem", on_delete=models.CASCADE, null=True,
                                blank=True)
    solution = models.OneToOneField('content', related_name="question_solution", on_delete=models.CASCADE, null=True,
                                    blank=True)
    AC = models.PositiveIntegerField(verbose_name="全对人数")
    priority = (
        (0, "关键"),
        (1, "重要"),
        (2, "一般"),
        (3, "用处较小"),
    )
    general_priority = models.SmallIntegerField(choices=priority, verbose_name="优先度")
    group = models.ManyToManyField('Group', blank=True, verbose_name="分组")
    ans = models.OneToOneField('Answer', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    def __str__(self):
        return self.ID

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "题目"
        verbose_name_plural = "题目"


class content(models.Model):
    stem_type = (
        ("txt", "text"),
        ("img", "image")
    )
    type = models.CharField(max_length=15, choices=stem_type, verbose_name="题干类型")
    img = models.FileField(upload_to="img/%Y/%m/%d", blank=True)
    text = models.TextField(blank=True)
    next_content = models.OneToOneField('content', related_name="prev_content", on_delete=models.CASCADE, null=True,
                                        blank=True)


class Chioce(models.Model):
    tp = (
        (0, '图片'),
        (1, '文字'),
        (2, '数字'),
    )
    ID = models.PositiveIntegerField(primary_key=True)
    related_question = models.ForeignKey('Question', null=True, blank=True, related_name='c_question',
                                         verbose_name='所属问题',
                                         on_delete=models.CASCADE)
    Bool = models.BooleanField(default=True, verbose_name="正确标志")
    type = models.IntegerField(choices=tp, verbose_name="类型")
    text = models.TextField(blank=True, verbose_name="文字")
    number = models.IntegerField(blank=True, verbose_name="数字")
    create_by = models.ForeignKey(User, null=True, blank=True, verbose_name='创建人', related_name="choice_creater",
                                  on_delete=models.SET_NULL)
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='最新修改日期')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    def __str__(self):
        return self.ID

    class Meta:
        ordering = ["-ID"]
        verbose_name = "选项"
        verbose_name_plural = "选项"


class Answer(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    related_question = models.ForeignKey('Question', null=True, blank=True, related_name='a_question',
                                         verbose_name='所属问题',
                                         on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name="文字")
    create_by = models.ForeignKey(User, null=True, blank=True, verbose_name='创建人', related_name='ans_creater',
                                  on_delete=models.SET_NULL)
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    modify_by = models.ForeignKey(User, null=True, blank=True, verbose_name='编辑人', related_name='ans_modifier',
                                  on_delete=models.SET_NULL)
    m_time = models.DateTimeField(auto_now=True, verbose_name='最新修改日期')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    def __str__(self):
        return self.ID

    class Meta:
        ordering = ["-ID"]
        verbose_name = "选项"
        verbose_name_plural = "选项"


class Chioce_tips(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    related_question = models.ForeignKey(Chioce, null=True, blank=True, related_name='t_question', verbose_name='所属选项',
                                         on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name="文字")
    # img = models.FilePathField(null=True, verbose_name="图片")
    create_by = models.ForeignKey(User, null=True, blank=True, verbose_name='创建人', related_name="tips_creater",
                                  on_delete=models.SET_NULL)
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='最新修改日期')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    def __str__(self):
        return self.ID

    class Meta:
        ordering = ["-ID"]
        verbose_name = "错误选项提示"
        verbose_name_plural = "错误选项提示"


class Record(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    related_question = models.OneToOneField('Question', null=True, blank=True, related_name='r_question',
                                            verbose_name='所属问题', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='用户', related_name="r_user",
                             on_delete=models.CASCADE)
    begin_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    AC = models.BooleanField(default=False)
    end_time = models.DateTimeField(auto_now_add=True, verbose_name='完成日期')
    duration = models.DurationField()
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    def __str__(self):
        return self.ID

    class Meta:
        ordering = ["-ID"]
        verbose_name = "记录"
        verbose_name_plural = "记录"


class Tag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=32, unique=True)
    c_day = models.DateField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"


class EventLog(models.Model):
    """
    日志.
    在关联对象被删除的时候，不能一并删除，需保留日志。
    因此，on_delete=models.SET_NULL
    """

    name = models.CharField('事件名称', max_length=128)
    event_type_choice = (
        (0, '其它'),
        (1, '添加/删除问题'),
        (2, '编辑问题'),
        (3, '问题管理'),
        (4, '添加测试'),
        (5, '定期维护'),
        (6, '用户管理添加\删除'),
        (7, '用户管理更新'),
    )
    quesion = models.ForeignKey('Question', blank=True, null=True, on_delete=models.SET_NULL)  # 当编辑问题时有这项数据
    target_user = models.ForeignKey(User, blank=True, null=True, verbose_name="目标用户", related_name='target_user',
                                    on_delete=models.SET_NULL)  # 当用户管理时有这项数据
    record = models.ForeignKey('Record', blank=True, null=True, on_delete=models.SET_NULL)  # 当讨论管理时有这项数据
    event_type = models.SmallIntegerField('事件类型', choices=event_type_choice, default=5)
    component = models.CharField('事件子项', max_length=256, blank=True, null=True)
    detail = models.TextField('事件详情')
    date = models.DateTimeField('事件时间', auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='事件执行人', related_name='execute_user',
                             on_delete=models.SET_NULL)
    memo = models.TextField('备注', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '事件纪录'
        verbose_name_plural = "事件纪录"


class Group(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField('分组名', max_length=32, unique=True)
    create_by = models.ForeignKey(User, null=True, blank=True, verbose_name='创建人', related_name="Group_creater",
                                  on_delete=models.SET_NULL)
    c_day = models.DateField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"
