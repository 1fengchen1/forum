from django.contrib import admin
from .models import Article
from comments.models import Comment

class CommentInline(admin.TabularInline):       #StackedInline和TabularInline是两种展示内联表的不同方式
    model = Comment
    can_delete = False

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "id", "title", "content", "owner")
    readonly_fields = ("owner", "content", "status", "create_timestamp")    #设置只读字段
    actions = ["make_picked"]           #设置动作
    inlines = [CommentInline]           #内连评论

    #将article的数据分组
    fieldsets = (
        ("基本", {"classes":('wide',), "fields":("title", "content")}),
        ("高级", {"classes": ('collapse',), "fields": ('status','create_timestamp')})
    )

    def make_picked(self, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = "设置精华"

admin.site.register(Article, ArticleAdmin)