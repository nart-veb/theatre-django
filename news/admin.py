from django.contrib import admin

from news.models import News, NewsImage


admin.site.register(News)
admin.site.register(NewsImage)
