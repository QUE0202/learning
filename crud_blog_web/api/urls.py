from django.urls import path
from crud_blog_web.views import index, indexArticle, indexArticleJson
urlpatterns = [
    path('test/', index),
    path('html/', indexArticle),
    path('articles/', indexArticleJson),
]