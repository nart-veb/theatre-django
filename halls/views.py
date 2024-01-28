from django.shortcuts import render
from django.views.generic.base import View
from halls.models import Hall,HallImage

class HallList(View):

    def get(self, request):
        hall_list = Hall.objects.all()
        hall_img_list = HallImage.objects.all()
        return render(request, 'hall/hall_list.html', context={'hall_list': hall_list,'hall_img_list': hall_img_list})

# Create your views here.
