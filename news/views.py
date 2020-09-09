from django.shortcuts import render, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    data = {
        'allData': Blog.objects.all(),
        'fashionData':Blog.objects.filter(main_menu__name = 'Fashion')[:4],
        'latestData': Blog.objects.all().order_by('created_at')[:5],
        'popularPost':Blog.objects.all().order_by('-page_visit')[:4],
        'technologyData':Blog.objects.filter(main_menu__name = 'Fashion'),
        'sportsData': Blog.objects.filter(main_menu__name='Fashion')[:4],
        'sportsDataMax':Blog.objects.filter(main_menu__name='Fashion').order_by('-page_visit')[:1],
        'mobileData':Blog.objects.filter(main_menu__name = 'Mobile'),
    }
    return render(request, 'pages/index.html',data)


def blog(request, slug):
    related = get_object_or_404(Blog, slug=slug)
    data = {
        'title': Blog.objects.get(slug=slug),
        'menuDetails': Blog.objects.get(slug=slug),
        'popularPost': Blog.objects.all().order_by('-page_visit')[:4],
        'relatedPost': related.tags.similar_objects()
    }
    return render(request, 'pages/details.html',data)


def details(request):
    data={
        'popularPost': Blog.objects.all().order_by('-page_visit')[:4],
    }
    return render(request, 'pages/category.html',data)


def mainmenudetails(request, name):
    # main_menu: MainMenu.objects.get(slug=slug)
    # main_menu.page_visit += 1
    # main_menu.save()
    data = {
        'title': MainMenu.objects.get(name=name),
        'menuDetails': Blog.objects.filter(main_menu__name = name),
        'popularPost': Blog.objects.all().order_by('-page_visit')[:4],
    }
    return render(request, 'pages/category.html', data)


def submenudetails(request, name):
    data = {
        'title': SubMenu.objects.get(name=name),
        'menuDetails': Blog.objects.filter(sub_menu__name=name),
        'popularPost': Blog.objects.all().order_by('-page_visit')[:4],
    }
    return render(request, 'pages/category.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')