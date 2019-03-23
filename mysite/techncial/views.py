from django.views import generic

from .models import Technical


class Techo(generic.ListView):

    template_name = 'techncial/tehome.html'

    def get_queryset(self):
        return Technical.objects.all()
