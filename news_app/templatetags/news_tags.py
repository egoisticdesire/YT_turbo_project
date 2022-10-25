from django import template
from django.db.models import Count, F

from news_app.models import Category

register = template.Library()


@register.simple_tag(name='get_all_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag(filename='news_app/inc/_sidebar.html')
def show_sidebar_categories():
    categories = Category.objects.annotate(
        cnt=Count(
            'news',
            filter=F('news__is_published'),
        )
    ).filter(cnt__gt=0)
    return {'categories': categories}
