
from django.template.defaulttags import register


## get key and return value from dict
@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)
