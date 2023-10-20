from django.conf import settings
from django import template
import json
from app.helpers import deep_get

register = template.Library()

language = {}

for lang in settings.LANGUAGES:
    with open(f'{settings.BASE_DIR}/locale/{lang[0]}.json', 'r', encoding='utf8') as file:
        language[lang[0]] = json.load(file)


@register.simple_tag(name="translate", takes_context=True)
def translate(context, value):
    lang = context['request'].LANGUAGE_CODE
    try:
        return deep_get(language[lang], value)
    except:
        return f"Not exists in /locale/{lang}.json"


@register.simple_tag(name="lang_font", takes_context=True)
def langFont(context):
    lang = context['request'].LANGUAGE_CODE
    if lang == "en":
        return "noto-regular"
    elif lang == "ur":
        return "font-arial"


@register.simple_tag(name="lang_dir", takes_context=True)
def langDir(context):
    lang = context['request'].LANGUAGE_CODE
    if lang == "en":
        return "ltr"
    elif lang == "ur":
        return "rtl"
