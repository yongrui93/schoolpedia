from django import template

register = template.Library()


@register.filter(name='is_bookmarked')
def is_bookmarked(school, user):
    return school.bookmark_set.filter(user=user).exists()


@register.filter(name='is_compared')
def is_compared(school, request):
    compare_school_id_list = request.session.get('compare_school_id_list', [])
    return str(school.id) in compare_school_id_list
