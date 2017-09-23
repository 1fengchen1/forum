from django.db import models
from django.contrib.auth.models import User

class ActivateCode(models.Model):

    username = models.CharField("用户名", max_length=20)
    activation_code = models.CharField("激活码", max_length=1000)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "激活码列表"
        verbose_name_plural = "激活码"
