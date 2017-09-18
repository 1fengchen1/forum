from django import forms
from .models import Article

'''参数校验器'''
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
