from django.urls import path
from people.views import PeopleList

urlpatterns = [
    path('', PeopleList.as_view(), name="people_list"),
]
