from django import template
from django.db.models  import Count, Q
from news.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('views')).filter(cnt__gt=0)

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='hello', arg2='world'):
    categories = Category.objects.annotate(cnt=Count('news', filter=Q(news__is_published=True))).filter(cnt__gt=0)
    return {"categories": categories, 'arg1':arg1,'arg2':arg2}