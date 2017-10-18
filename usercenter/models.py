from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,   #一对一外键
            on_delete=models.CASCADE)
    sex = models.IntegerField("性别",
            choices=((0, "男"),(1, "女")), default=0)
    birthday = models.DateTimeField("生日",
                null=True, blank=True)
    avatar = models.CharField("头像地址",
                max_length=300, blank=True)             #blank设置为True时，可以为空；为False时，不可以为空

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"