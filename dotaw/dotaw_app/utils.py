from django.core.cache import cache
from .models import Position

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        c = cache.get('cat_list')
        if c is None:
            cat_list = Position.objects.all()
            cache.set('cat_list', cat_list, 60*60*24*3651)
        context['cat_list'] = cat_list
        return context

