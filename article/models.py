from django.db import models
from blocks.models import Block
from django.contrib.auth.models import User

class Article(models.Model):

    owner = models.ForeignKey(User, verbose_name="作者")
    block = models.ForeignKey(Block, verbose_name="板块名") #Block表结构外键的引用
    title = models.CharField("文章标题", max_length=100)
    content = models.CharField("文章内容", max_length=10000)
    status = models.IntegerField("状态",
            choices=((0, "正常"), (-1, "删除")))

    #创建时间
    create_timestamp = models.DateTimeField("创建时间", auto_now_add=True)
    #最后更新时间
    last_timestamp = models.DateTimeField("最后更新时间", auto_now=True)

    def __str__(self):                  #将title展示在列表下并汉化
        return self.title

    class Meta:
        verbose_name = "文章"                     #后台列表表名
        verbose_name_plural = "文章"              #后台外层展示名