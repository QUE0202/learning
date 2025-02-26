from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from crud_blog_web.models import Article

def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def indexArticle(request):
    title = "Lista Artykułów"
    articles = Article.objects.all()
    return render(request, "articles.html", {
        "articles": articles,
        "title": title,
    })