from django import template

register = template.Library()

@register.filter(name='enumerate')
def enumerate_filter(sequence):
    return enumerate(sequence)

@register.filter
def intcomma(value):
    try:
        value = int(value)
        return "{:,}".format(value)
    except (ValueError, TypeError):
        return value
