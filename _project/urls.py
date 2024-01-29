from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from _project.views import Index
from radio.views import AudioList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('posters/', include('perfomances.urls'), name='poster'),
    path('radio/', AudioList.as_view(), name="radio"),
    path('people/', include('people.urls'), name="people"),
    path('history/', include('histories.urls'), name="history"),
    path('halls/', include('halls.urls'), name="halls"),
    path('press/', include('press.urls'), name="press"),
    path('news/', include('news.urls'), name="news"),
    path('partner/', include('partners.urls'), name="partner")
]

# For debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
