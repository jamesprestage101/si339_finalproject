from django import template

register = template.Library()

@register.filter
def get_lat(geopt):
    """
    Gets the latitude from a GeoPt object
    Usage: {{ geopt|get_lat }}
    """
    if geopt:
        return geopt.lat
    return 53.350140  # Default latitude

@register.filter
def get_lng(geopt):
    """
    Gets the longitude from a GeoPt object
    Usage: {{ geopt|get_lng }}
    """
    if geopt:
        return geopt.lon
    return -6.266155  # Default longitude