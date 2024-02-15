from django.shortcuts import render
from django.views.generic.base import View
from press.models import Press


# Create your views here.
class PressList(View):

    def get(self, request):
        press_list = Press.objects.all()
        return render(request, 'press/press_list.html', context={'press_list': press_list,})


class PressDetail(View):

    def get(self, request, pk=None):
        press = (
            Press
            .objects
            .get(id=pk)
        )
        return render(request,
                      'press/press_detail.html',
                      context={
                          'item': press,
                      }
                      )
