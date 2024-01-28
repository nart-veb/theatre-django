from django.urls import path
from histories.views import HistoryList, HistoryDetail

urlpatterns = [
    path('', HistoryList.as_view(), name="histories_list"),
    path('<int:pk>/', HistoryDetail.as_view(), name="histories_detail"),
]
