from django.contrib import admin

from people.models import Person, Position,PersonCategory

admin.site.register(Person)
admin.site.register(PersonCategory)
admin.site.register(Position)