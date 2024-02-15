from django.urls import path
from halls.views import HallList

urlpatterns = [
    path('', HallList.as_view(), name="hall_list"),
]
