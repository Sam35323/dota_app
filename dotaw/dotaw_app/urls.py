from .views import index, OneHero, Login, show_pagination, HeroList, CatList, Register, AddPage
from django.urls import path
from django.contrib.auth import views as authViews
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('perses/', cache_page(timeout=60)(HeroList.as_view()), name='persi'),
    path('one_hero/<slug:hero_slug>/', OneHero.as_view(), name='ohe_hero'),
    path('categories/<slug:cat_slug>/', CatList.as_view(), name='categories'),
    path('new_pers/', AddPage.as_view(), name='new_pers'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('test/', show_pagination),
    path('exit/', authViews.LogoutView.as_view(next_page='persi'), name='exit'),
]
