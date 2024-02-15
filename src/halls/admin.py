from django.contrib import admin

from halls.models import Hall, HallImage

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(HallImage)
class HallImageAdmin(admin.ModelAdmin):
    list_filter = ('hall',)

