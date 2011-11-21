from django import template
from django.db import models
from django.core.cache import cache
from django.contrib.sites.models import Site

register = template.Library()

Bunk = models.get_model('bunks', 'Bunk')
CACHE_PREFIX = "bunk_"

def do_get_bunk(parser, token):
	# split_contents() knows not to split quoted strings.
	tokens = token.split_contents()
	if len(tokens) < 2 or len(tokens) > 3:
		raise template.TemplateSyntaxError, "%r tag should have either 2 or 3 arguments" % (tokens[0],)
	if len(tokens) == 2:
		tag_name, key = tokens
		cache_time = 0
	if len(tokens) == 3:
		tag_name, key, cache_time = tokens
	# Check to see if the key is properly double/single quoted
	if not (key[0] == key[-1] and key[0] in ('"', "'")):
		raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
	# Send key (without quotes) and caching time
	return BunkNode(key[1:-1], cache_time)
	
class BunkNode(template.Node):
	def __init__(self, key, cache_time=0):
	   self.key = key
	def render(self,context):
		bunk = Bunk.objects.get(key=self.key)
		return bunk.content

register.tag('bunk', do_get_bunk)
