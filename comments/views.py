from .jsonresponse import json_response
from .models import Comment
from article.models import Article

def comment_create(request):
    owner= request.user
    content = request.POST['content'].strip()
    article_id = request.POST["article_id"]
    article = Article.objects.get(id=article_id)
    if not content:
        error = {"status":"error","msg":"信息不能为空"}
        return json_response(error)
    comment = Comment(owner=owner, article=article,
                      content=content, status=0)
    comment.save()
    sucess = {"status":"ok"}
    return json_response(sucess)