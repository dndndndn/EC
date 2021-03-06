# coding=utf-8

from django.db import models

# Create your models here.


class User(models.Model):

    gender=(
        ("男",'male'),
        ("女",'female'),
    )
    admin=(
        ('admin',"管理员"),
        ('user', "用户"),
    )
    student_id = models.PositiveIntegerField(verbose_name="学号", unique=True)
    name = models.CharField(verbose_name="姓名",max_length=128)
    password = models.CharField(verbose_name="密码",max_length=256)
    email=models.EmailField(verbose_name="邮件地址",unique=True)
    sex=models.CharField(verbose_name="性别",max_length=32,choices=gender,default='female')
    c_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    Profile_photo = models.FileField(verbose_name="头像", upload_to='store/upload/%Y/%m/%d',
                                     default="img/default_handsome.jpg")
    auth = models.CharField(verbose_name="权限",max_length=128,choices=admin,default='user')
    school = models.CharField(verbose_name="学院",max_length=256,default="未知")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name="用户"
        verbose_name_plural="用户"
        unique_together = (('name','student_id'),)


class Group(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="分组名", max_length=20)
    members = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('group', 'user'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    invite_reason = models.CharField(max_length=64)
