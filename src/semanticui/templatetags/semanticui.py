from django import forms
from django.template.loader import get_template
from django import template

register = template.Library()


@register.filter
def semanticui(element):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    return render(element, markup_classes, False)


@register.filter
def semanticui_inline(element, label_cols=''):
    markup_classes = {'label': label_cols, 'value': '', 'single_value': ''}
    return render(element, markup_classes, True)


def render(element, markup_classes, is_inline):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("semanticui/field.html")
        context = {
            'field': element,
            'classes': markup_classes,
            'form': element.form,
            'is_inline': is_inline,
        }
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            template = get_template("semanticui/formset.html")
            context = {
                'formset': element,
                'classes': markup_classes,
                'is_inline': is_inline,
            }
        else:
            template = get_template("semanticui/form.html")
            context = {
                'form': element,
                'classes': markup_classes,
                'is_inline': is_inline,
            }
    return template.render(context)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_datetime(field):
    return isinstance(field.field.widget, forms.DateTimeInput)


@register.filter
def is_date(field):
    return isinstance(field.field.widget, forms.DateInput)


@register.filter
def is_date_range_start(field):
    return isinstance(field.field.widget, forms.DateInput) and field.name == 'start_date'


@register.filter
def is_date_range_end(field):
    return isinstance(field.field.widget, forms.DateInput) and field.name == 'end_date'


@register.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)
