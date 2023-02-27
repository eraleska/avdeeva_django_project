from django.shortcuts import render
from .models import Themes
from .models import News
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def forum_home(request):
    theme_list = Themes.objects.all()
    news_list = News.objects.order_by('-datenews')
    return render(request,'forum/news.html', {"th_list":theme_list, "news_list": news_list})
