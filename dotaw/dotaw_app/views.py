from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator

from .models import Hero, Position
from .forms import HeroForm
from .utils import DataMixin

cat_list = Position.objects.all()


def index(request):
    req = request.GET['gum']
    return HttpResponse(f'<h1>sf ohhh nooooo its cringe maaaaaaaan {req}<h1>')

class OneHero(DataMixin, DetailView):
    model = Hero
    template_name = 'dotaw_app/wanhero.html'
    context_object_name = 'hero'
    slug_url_kwarg = 'hero_slug'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

class HeroList(DataMixin, ListView):
    model = Hero
    template_name = 'dotaw_app/all_heroes.html'
    context_object_name = 'heroes'
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class CatList(DataMixin, ListView):
    model = Hero
    template_name = 'dotaw_app/all_heroes.html'
    context_object_name = 'heroes'
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(category_id=context['heroes'][0].top_position_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Hero.objects.filter(top_position__slug=self.kwargs['cat_slug'])


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = HeroForm
    template_name = 'dotaw_app/new_pers.html'
    raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

class Register(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'dotaw_app/registr.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'dotaw_app/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('persi'
                            '')

def show_pagination(request):
    list = Hero.objects.all()
    p = Paginator(list, 2)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'dotaw_app/test.html', {'page_obj': page_obj, 'paginator': p})