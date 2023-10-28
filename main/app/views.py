from django.views.generic import ListView, DetailView

from app.models import MenuItem


class ViewsHome(ListView):
    model = MenuItem
    template_name = 'app/index.html'
    context_object_name = 'menu'

class Show_obj(DetailView):
    model =MenuItem
    template_name = 'app/obj.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'menu'