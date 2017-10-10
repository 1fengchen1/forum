from .jsonresponse import json_response
from .models import Comment
from instationmsg.models import Message
from article.models import Article
from article.views import ArticleDetailView

def comment_create(request):
    owner= request.user                                             #登录人
    content = request.POST["content"].strip()                       #评论内容
    article_id = request.POST["article_id"]
    to_comment_id  = int(request.POST.get("to_comment"))         #回复的评论，默认为0
    article = Article.objects.get(id=article_id)                    #评论的文章
    if not content:                                                 #判断内容为空时
        error = {"status":"error","msg":"信息不能为空"}
        return json_response(error)
    if to_comment_id != 0:
        to_comment = Comment.objects.get(id=to_comment_id)
        owner_msg = to_comment.owner
        content_unmsg = "有人评论了你的评论：" + to_comment.content[0:20]+"..."
    else:
        to_comment = None
        owner_msg = article.owner
        content_unmsg = "有人评论了你的文章：" + article.title

    comment = Comment(owner=owner, article=article,                 #将要保存的内容放进comment对象
                      content=content, status=0, to_comment=to_comment)
    page_no= request.POST["page_no"]
    link = "/article/detail/" + str(article.id) + page_no
    message = Message(owner=owner_msg, content=content_unmsg, link=link, status=-1)
    comment.save()                                                  #将数据保存到数据库
    message.save()
    sucess = {"status":"ok"}
    return json_response(sucess)                                    #返回成功的字符串为json格式