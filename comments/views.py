from .jsonresponse import json_response
from .models import Comment
from article.models import Article
from article.sorter import paginate_queryset
from django.contrib.auth.decorators import login_required

#@login_required
def comment_create(request):
    owner= request.user
    content = request.POST['content'].strip()
    article_id = request.POST["article_id"]
    article = Article.ogjects.get(id=article_id)
    if not content:
        error = {"status":"error","msg":"信息不能为空"}
        return json_response(error)
    comment = Comment(owner=owner, article=article,
                      content=content, status=0)
    comment.save()
    print (comment)
    sucess = {"status":"ok"}
    return json_response(sucess)