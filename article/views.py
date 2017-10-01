from django.shortcuts import render
from blocks.models import Block
from article.models import Article
from django.shortcuts import redirect
from .forms import ArticleForm
from django.views.generic import  DetailView
from django.contrib.auth.decorators import login_required
from .sorter import paginate_queryset
from comments.models import Comment

'''文章列表页面处理方法'''
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)  #Block表的id列传给block参数
    all_articles = Article.objects.filter(block=block, status=0).order_by("-id")   #Article表的Block_id列和status=0的列传给articles_objs，并根据id降序排序
    page_no = int(request.GET.get("page_no", "1"))
    '''
    ##############做成工具###########
    ARTICLE_CNT_1PAGE = 3  # 定义一页多少数据
    p = Paginator(all_articles, ARTICLE_CNT_1PAGE)     #分页器实例p
    page = p.page(page_no)                              #提取第几页：参数page_no是GET的参数
    articles_objs = page.object_list                     #取出指定页的文章们
    #分页算法#
    page_cnt = p.num_pages                                      #总页数
    current_no = page_no                                        #当前页码
    page_links = [i for i in range(page_no-2, page_no+3)        #标页列表
                  if i > 0 and i <= p.num_pages]
    previous_link = page_links[0]-1                             #最小页-1
    next_link = page_links[-1]+1                                #最大页+1
    has_previous = previous_link > 0                            #有前页
    has_next = next_link <= page_cnt                            #有后页
    argument = { "b":block, "articles":articles_objs,
                "page_cnt":page_cnt, "current_no":current_no,
                "page_links":page_links, "previous_link":previous_link,
                "next_link":next_link, "has_previous":has_previous,
                "has_next":has_next}
    '''
    page_articles, pagination_data= paginate_queryset(all_articles, page_no, cnt_per_page=3)
    argument = {"articles":page_articles, "b":block, 'pagination_data':pagination_data}
    return render(request, 'article_list.html', argument)  #将响应返回给浏览器，第三个参数，htmll里面的参数填充



'''创建文章页面的GET处理方法和POST处理方法'''
@login_required
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
            article.owner = request.user
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)  #重定向页面(重新请求一个页面)，直接返回到模板下list的页面
        else:
            return render(request, "article_create.html", {"b":block, "form":form})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "a"

    #展示评论内容(在DetailView展示其他内容)
    def get_context_data(self, **kwargs):                                       #重载了context_object_name
        context = super().get_context_data(**kwargs)                            #context得到的字典{'a':文章的对象}
        page_no = int(self.request.GET.get("page_no", "1"))                     #当前页
        all_comments = Comment.objects.filter(article=context["a"],status=0)    #全量数据
        comments, pagination_data = paginate_queryset(all_comments,
                                    page_no, cnt_per_page=3)
        context['comments'] = comments                                          #这一页相关的评论(相当于render()的第三个参数)
        context['pagination_data'] = pagination_data                            #这一页相关的其他页
        return context                                                          #

