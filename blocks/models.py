from django.db import models    #Django规定使用数据库必须要导入的


class Block(models.Model):
    '''定义表结构，就是对类进行定义属性'''
    name = models.CharField("板块标题", max_length=100)  #设置列类型，名字，长度
    desc = models.CharField("板块描述", max_length=100)
    manager_name = models.CharField("管理员名字", max_length=100)
    status = models.IntegerField("状态",
            choices =((0, "正常"), (-1, "删除")))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "首页"     #在数据表内，添加板块的展示
        verbose_name_plural = "首页板块"  #数据表名展示


