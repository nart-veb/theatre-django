from django.shortcuts import render
from django.views.generic.base import View
from people.models import Person,PersonCategory


# Create your views here.
class PeopleList(View):
    def get(self, request):
        people_list = Person.objects.all()
        category_list = PersonCategory.objects.order_by("sorting")
        return render(request, 'people/people_list.html', context={'people_list': people_list, 'category_list': category_list})