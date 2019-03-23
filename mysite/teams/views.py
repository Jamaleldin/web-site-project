from django.views import generic

from .models import Team


class Teamo(generic.ListView):

    template_name = 'teams/thome.html'

    def get_queryset(self):
        return Team.objects.all()
