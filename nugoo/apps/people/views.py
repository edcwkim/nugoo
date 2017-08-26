from django.http import JsonResponse
from django.views import generic
from .models import Person


class PersonDetail(generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/person-detail.html.dj'


class PersonListByName(generic.ListView):
    context_object_name = 'people'
    template_name = 'people/person-list-by-name.html.dj'

    def get_queryset(self):
        return Person.objects.filter(name=self.kwargs['name'])


class PersonListName(generic.ListView):
    model = Person

    def get(self, request, *args, **kwargs):
        names = self.get_queryset().values_list('name', flat=True)
        return JsonResponse({
            'data': list(names),
        })
