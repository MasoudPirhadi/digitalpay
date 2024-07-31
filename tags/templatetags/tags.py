from django import template

register = template.Library()


@register.filter(name='three_digits_currency')
def three_digits_currency(value):
    if value is not None:
        return '{:,}'.format(value) + ' تومان '
    else:
        return '0'.format(value) + ' تومان '


@register.filter(name='three_digits')
def three_digits_currency(value):
    if value is not None:
        return '{:,}'.format(value)
    else:
        return '0'.format(value)

