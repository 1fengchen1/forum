from django.db import models

class Message(models.Model):

    owner = models.CharField('谁的消息', max_length=20)
    content = models.CharField('消息内容', max_length=30)
    link = models.CharField('链接', max_length=50)
    status = models.IntegerField('状态',
            choices=((-1, "未读"),(0, "删除"),(1, "已读")))

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = "未读的站内信"
        verbose_name_plural = "未读的站内信"