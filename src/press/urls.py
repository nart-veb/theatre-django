from django.urls import path
from press.views import PressList, PressDetail

urlpatterns = [
    path('', PressList.as_view(), name="press_list"),
    path('<int:pk>/', PressDetail.as_view(), name="press_detail"),
]
