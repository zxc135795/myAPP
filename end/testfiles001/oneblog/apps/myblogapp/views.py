from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page
# from .forms import *
from time import *


# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器


# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表


# Create your views here.
def index(request):
    recommends = Recommend.objects.all()[:3:]
    ads = Ads.objects.all()
    note = Note.objects.all().order_by('-note_time')
    articles = Article.objects.all().order_by('-create_time')
    paginator = Paginator(articles, 3)
    num = request.GET.get('pagenum', 1)
    page = paginator.get_page(num)
    # articles.save()
    artc = articles[:3:]
    return render(request, 'index.html', locals())


def detail(request, articleid):
    try:
        notes = Note.objects.all()
        artic = Article.objects.all()
        recommends = Recommend.objects.all()[:3:]
        articles = Article.objects.filter(id=articleid)
        artc = artic[:3:]
        print(articles)

        return render(request, 'article.html', locals())
    except Exception as e:
        print(e)
        return HttpResponse('错误')

    # return render(request, 'article.html', locals())


# def contact(request):
#     return render(request, 'contact.html')


def favicon(request):
    return redirect(to='/static/favicon.ico')


#

def list(request):
    recommends = Recommend.objects.all()[:3:]
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    num = request.GET.get('pagenum', 1)
    page = paginator.get_page(num)
    artc = articles[:3:]
    return render(request, 'list.html', locals())


def aboutme(request):
    recommends = Recommend.objects.all()[:3:]
    articles = Article.objects.all()
    artc = articles[:3:]
    return render(request, 'about_me.html', locals())


def note(request):
    recommends = Recommend.objects.all()[:3:]
    articles = Article.objects.all()
    artc = articles[:3:]
    notes = Note.objects.all()
    return render(request, 'recomment.html', locals())
