from django.shortcuts import render
from blocks.models import Block
from article.models import Article
from django.shortcuts import redirect
from .forms import ArticleForm

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
        return render(request, 'article_create.html', {"b": block})
    else:
        form = ArticleForm(request.POST)    #参数校验器实例化
        if form.is_valid():             #参数合法
            article = form.save(commit=False)   #form校验器里面的属性都赋值给article对象，并不存进数据库，对象还在内存中
            article.block = block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)  #重定向页面(重新请求一个页面)，直接返回到模板下list的页面
        else:
            return render(request, "article_create.html", {"b":block, "form":form})

