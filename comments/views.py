from .jsonresponse import json_response
from .models import Comment
from article.models import Article

def comment_create(request):
    owner= request.user                                             #登录人
    content = request.POST['content'].strip()                       #评论内容
    article_id = request.POST["article_id"]

    article = Article.objects.get(id=article_id)                    #评论的文章
    if not content:                                                 #判断内容为空时
        error = {"status":"error","msg":"信息不能为空"}
        return json_response(error)
    comment = Comment(owner=owner, article=article,                 #将要保存的内容放进comment对象
                      content=content, status=0)

    comment.save()                                                  #将数据保存到数据库
    sucess = {"status":"ok"}
    return json_response(sucess)                                    #返回成功的字符串为json格式