from django.http import HttpResponse
from django.shortcuts import render
from .models import Hero, Position

cat_list = Position.objects.all()

def index(request):
	req = request.GET['gum']

	return HttpResponse(f'<h1>sf ohhh nooooo its cringe maaaaaaaan {req}<h1>')


def one_hero(request, hero_slug):

	hero = Hero.objects.get(slug=hero_slug)

	context = {'heh': hero, 'cat_list': cat_list, 'category_id': hero.top_position.id}
	return render(request, 'dotaw_app/wanhero.html', context=context)

def pers_list(request):
	heroes = Hero.objects.all()

	context = {'heroes': heroes, 'cat_list': cat_list}
	return render(request, 'dotaw_app/all_heroes.html', context=context)


def categories(request, category_id):
	heroes = Hero.objects.filter(top_position_id=category_id)
	context = {'heroes': heroes, 'category_id': category_id, 'cat_list': cat_list}
	return render(request, 'dotaw_app/all_heroes.html', context=context)

