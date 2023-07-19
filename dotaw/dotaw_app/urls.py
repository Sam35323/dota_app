from .views import index, one_hero, pers_list, categories
from django.urls import path


urlpatterns = [
    path('perses', pers_list, name='persi'),
    path('one_hero/<slug:hero_slug>/', one_hero, name='ohe_hero'),
    path('categories/<int:category_id>/', categories, name='categories'),
]
