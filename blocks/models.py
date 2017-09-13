from django.db import models

class Block(models.Model):
    name = models.CharField("模板标题", max_length=100)
    desc = models.CharField("模板描述", max_length=100)
    manager_name = models.CharField("管理员名字", max_length=100)
