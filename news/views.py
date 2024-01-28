from django.shortcuts import render
from django.views.generic.base import View
from news.models import News


# Create your views here.
class NewsList(View):

    def get(self, request):
        news_list = News.objects.all()
        return render(request, 'news/news_list.html', context={'news_list': news_list,})


class NewsDetail(View):

    def get(self, request, pk=None):
        news = (
            News
            .objects
            .get(id=pk)
        )
        return render(request,
                      'news/news_detail.html',
                      context={
                          'item': news,
                      }
                      )
