from django.contrib import admin
from .models import Event, Hashtag, Person, PersonToEvent

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(PersonToEvent)
admin.site.register(Hashtag)
