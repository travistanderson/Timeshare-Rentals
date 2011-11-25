# ts/templatetags/date_range.py
from django import template

# {% date_range ad.start_room ad.end_room %}   sample syntax


register = template.Library()

@register.tag(name='display_range')
def do_display_range(parser,token):
	try:
		tag_name, start, end = token.split_contents()
	except ValueError:
		raise tmplate.TemplateSyntaxError("%r tag requires two arguments" % token.contents.split()[0])
	return DisplayRanger(start,end)


class DisplayRanger(template.Node):
	"""Displays date range of two dates"""
	def __init__(self, start,end):
		self.start = template.Variable(start)
		self.end = template.Variable(end)

	def render(self, context):
		start = self.start.resolve(context)
		end = self.end.resolve(context)
		if start.year == end.year:
			if start.month == end.month:
				return start.strftime('%b %d') + ' - ' + end.strftime('%d, %Y')
			else:
				return start.strftime('%b %d') + ' - ' + end.strftime('%b %d, %Y')
		else:
			return start.strftime('%b %d, %Y') + ' - ' + end.strftime('%b %d, %Y')
		
	
		
		
