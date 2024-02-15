from django.shortcuts import render
from django.views.generic.base import View
from histories.models import History


# Create your views here.
class HistoryList(View):

    def get(self, request):
        histories_list = History.objects.all()
        return render(request, 'histories/histories_list.html', context={'histories_list': histories_list,})


class HistoryDetail(View):

    def get(self, request, pk=None):
        history = (
            History
            .objects
            .get(id=pk)
        )
        return render(request,
                      'histories/histories_detail.html',
                      context={
                          'item': history,
                      }
                      )
