from django.urls import path
from partners.views import PartnerList

urlpatterns = [
    path('', PartnerList.as_view(), name="partner_list"),
]
