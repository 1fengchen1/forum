from django.db import models
from article.models import Article

class Comment(models.Model):

    article = models.ForeignKey(Article, verbose_name="文章")
    owner = models.CharField("评论人", max_length=20)
    content = models.CharField("评论内容", max_length=10000)
    status = models.IntegerField("状态",
            choices=((0, "正常"),(-1, "删除")))
    create_timestamp = models.DateTimeField("创建时间", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.owner

    class Mate:
        verbose_name = "评论内容"
        verbose_name_plural = "评论内容"