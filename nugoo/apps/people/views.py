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
        qs = Person.objects.all()
        if qs:
            names = qs.values_list('name', flat=True).distinct()
            people_by_name = []
            for name in names:
                people = []
                for person in qs.filter(name=name):
                    person_values = {
                        'hashtags': list(person.get_hashtag_names()),
                        'photo__url': person.get_photo_absolute_uri(request),
                    }
                    stat = person.get_stat()
                    if stat:
                        person_values['stat__name'] = stat.name
                        person_values['stat__value'] = stat.value
                    people.append(person_values)
                people_by_name.append(people)
            return JsonResponse(dict(zip(names, people_by_name)))
        else:
            raise Http404
