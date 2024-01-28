from django.shortcuts import render
from django.views.generic.base import View
from partners.models import Partner

# Create your views here.
class PartnerList(View):

  def get(self, request):
      partner_list = Partner.objects.all()
      return render(request, 'partners/partners_list.html', context={'partner_list': partner_list})