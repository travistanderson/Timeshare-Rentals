# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
# from photologue.models import Photo


# here is my custom one to fix the underscore problem
class travEditor(forms.Textarea):
	class Media:
		js = ('/admin_media/js/traveditor/traveditor.js',)
		css = {'all':('/admin_media/css/traveditor.css',)}
	
	def __init__(self, language=None, attrs=None):
		# self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'cols':'70'}
		if attrs:
		    self.attrs.update(attrs)
		super(travEditor, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(travEditor, self).render(name, value, attrs)
		return rendered + mark_safe(u'''
			<div class="wmd-preview"></div>		
		''')



class WMDEditor(forms.Textarea):
	class Media:
		css = {
			'all': ('/site_media/css/wmd.css',)
		}
		js = ('/site_media/javascript/wmd.js',)
		
	def __init__(self, *args, **kwargs):
		attrs = kwargs.setdefault('attrs', {})
		if 'cols' not in attrs:
			attrs['cols'] = 108
		if 'rows' not in attrs:
			attrs['rows'] = 10
		attrs['id'] = 'wmd-input'
		attrs['class'] = 'wmd-panel'
		attrs['width'] = '650px'
		super(WMDEditor, self).__init__(*args, **kwargs)

	def render(self, name, value, attrs=None):
		rendered = super(WMDEditor, self).render(name, value, attrs)
		return mark_safe(u'''<div id="wmd-button-bar" class="wmd-panel"></div><div id="wmd-input-wrapper" style="margin:0 0 0 210px;width:800px;">''') + rendered + mark_safe(u'''</div>
			<span style="margin:0 0 0 210px;color:#417690">Preview</span>
			<span id="wmd-preview" class="wmd-panel post" style="height:500px;width:800px;"></span>
			<script type="text/javascript">
				wmd_options = {
					 output: "HTML",
					 buttons: "bold italic | link blockquote code image | ol ul heading"
				};
				</script>
		''')



class WMDEditor2(forms.Textarea):

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        if 'cols' not in attrs:
            attrs['cols'] = 58
        if 'rows' not in attrs:
            attrs['rows'] = 8
        super(WMDEditor2, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        rendered = super(WMDEditor2, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            wmd_options = {
                output: "HTML",
                buttons: "bold italic | link blockquote code image | ol ul"
            };
            </script>
            <script type="text/javascript" src="/site_media/javascript/wmd/wmd.js"></script>''')



# class WYMEditor(forms.Textarea):
#	  class Media:
#			js = (
#				 'jquery/jquery.js',
#				 'wymeditor/jquery.wymeditor.pack.js',
#			)
# 
#	  def __init__(self, language=None, attrs=None):
#			self.language = language or settings.LANGUAGE_CODE[:2]
#			self.attrs = {'class': 'wymeditor'}
#			if attrs:
#				 self.attrs.update(attrs)
#			super(WYMEditor, self).__init__(attrs)
# 
#	  def render(self, name, value, attrs=None):
#			rendered = super(WYMEditor, self).render(name, value, attrs)
#			return rendered + mark_safe(u'''<script type="text/javascript">
#				 jQuery('#id_%s').wymeditor({
#					  updateSelector: '.submit-row input[type=submit]',
#					  updateEvent: 'click',
#					  lang: '%s',
#				 });
#				 </script>''' % (name, self.language))




# {# <form action="/discuss/new" method="POST"> #}
# <div id="wmd-button-bar" class="wmd-panel"></div>

#	  <div id="wmd-button-bar" class="wmd-panel"></div>
#	  <div id="wmd-input-wrapper">
#	  	<textarea id="wmd-input" class="wmd-panel"></textarea>
#	  </div>
#	  <span id="wmd-preview" class="wmd-panel post" style="height:500px;"></span>
# {# </form> #}
# <script type="text/javascript" src="{{ COMMON_PATH }}javascript/wmd.js"></script>
