from django.shortcuts import render
from blocks.models import Block
from article.models import Article
from django.shortcuts import redirect

'''文章列表页面处理方法'''
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)  #Block表的id列传给block参数
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")   #Article表的Block_id列和status=0的列传给articles_objs，并根据id降序排序
    return render(request, 'article_list.html', {'articles':articles_objs, "b":block})  #将响应返回给浏览器，第三个参数，htmll里面的参数填充

'''创建文章页面的GET处理方法和POST处理方法'''
def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    if request.method == "GET":     #填写页面
        return render(request, 'article_create.html',
                      {"b": block,})
    else:
        title = request.POST["title"].strip()  #strip()去除字符串两边的空白及回车
        content = request.POST["content"].strip()
        if not (title and content):            #标题或内容空值校验
            return render(request, "article_create.html",
                          {"b":block, "error":"标题和内容不能为空."})
        if len(title) > 100 or len(content) > 10000:        #长度校验
            return render(request, "article_create.html",
                          {"b":block, "error":"标题或内容太长."})

        article = Article(block=block, title=title, content=content, status=0)  #将create文章页面创建一行数据
        article.save()                                                          #将数据存入数据库
        return redirect("/article/list/%s" % block_id)  #重定向页面(重新请求一个页面)，直接返回到模板下list的页面