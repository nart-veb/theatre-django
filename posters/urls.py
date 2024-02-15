from django.urls import path

from posters.views import PosterList, PosterDetail, Place, Map, Ticket

appname = "posters"

urlpatterns = [
    path('', PosterList.as_view(), name="poster-list"),
    path('<int:pk>/', PosterDetail.as_view(), name="poster-detail"),
    path('<int:pk>/place/', Place.as_view(), name="poster-places"),
    path('<int:pk>/place/get-map/', Map.as_view(), name="poster-places-map"),
    path('<int:pk>/place/get-tickets/', Ticket.as_view(), name="poster-places-tickets")
]
