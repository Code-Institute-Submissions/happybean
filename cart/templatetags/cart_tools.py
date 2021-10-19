"""
Template tags for Cart
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Template tags for Cart to calculate subtotal
    """
    return price * quantity
