from django.apps import apps
from django.db.models import Q
from django.views import generic

Person = apps.get_model('people.Person')


class Home(generic.ListView):
    context_object_name = 'people'
    template_name = 'core/home.html.dj'

    def get_queryset(self):
        return Person.objects.exclude(
            Q(hashtags__isnull=True) | Q(stat_set__isnull=True),
        ).order_by('?')
