from django.http import Http404, JsonResponse
from django.views import generic
from .models import Person


class PersonDetail(generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/person-detail.html.dj'


class PersonListByName(generic.ListView):
    context_object_name = 'people'
    template_name = 'people/person-list-by-name.html.dj'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['X-Frame-Options'] = 'ALLOWALL'
        return response

    def get_queryset(self):
        return Person.objects.filter(name=self.kwargs['name'])


class PersonList(generic.View):

    def get(self, request, *args, **kwargs):
        people = Person.objects.all()
        if people:
            names = people.values_list('name', flat=True).distinct()
            people_by_name = [list(people.filter(name=name)) for name in names]
            return JsonResponse(zip(names, people_by_name))
        else:
            raise Http404
