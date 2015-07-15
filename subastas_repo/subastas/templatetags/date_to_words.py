from django import template

from subastas.date_to_words import numero_a_palabra, numero_a_mes

register = template.Library()


@register.filter
def mes_literal(date):
    return numero_a_mes(date.month)


@register.filter
def dia_literal(date):
    return numero_a_palabra(date.day)


@register.filter
def hora_literal(date):
    return numero_a_palabra(date.hour)
