from django.views import generic
from .models import Person


class PersonDetail(generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/person-detail.html.dj'
