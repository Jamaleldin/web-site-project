from django.views import generic

from .models import STUnion


class Union(generic.ListView):

    template_name = 'union/Uhome.html'

    def get_queryset(self):
        return STUnion.objects.all()
