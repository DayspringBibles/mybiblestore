from django import template
register = template.Library()
from django.conf import settings

import os

@register.filter(name='human_readable')
def human_readable(value):
	value = value.replace('_',' ')
	return value
	
@register.filter(name='get_item_images')
def get_item_images(value):
	filelist = [filename for filename in os.listdir(settings.MY_STATIC_ROOT) if filename.startswith(value)]

	return filelist
	
@register.filter(name='get_item_thumb')
def get_item_thumb(value):

	try:
		file = [filename for filename in os.listdir(settings.MY_STATIC_ROOT) if filename.startswith('thumb_' + value)][0]
	except:
		file = 'missing.png'

	return file


@register.filter(name='get_cover_image')
def get_cover_image(value):

	try:
		file = [filename for filename in os.listdir(settings.MY_STATIC_ROOT) if filename.startswith(value)][0]
	except:
		file = 'missing_leather.png'

	return file