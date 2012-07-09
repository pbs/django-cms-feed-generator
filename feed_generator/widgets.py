from django.forms.util import flatatt
from django.forms.widgets import TextInput
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode



class ImageWidget(TextInput):
    """
        Add possibility to browse the filer for an image
    """
    def render(self, name, value, attrs=None):
        attrs.update({'value': force_unicode(self._format_value(value)) if value else ''})
        attrs.update(self.attrs)

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        image_input_id=final_attrs.get('id')
        filer_url = reverse('admin:filer_folder_changelist')
        getfile_url = reverse('feed_generator.views.get_file')

        html_browse_inclusion = '<script type="text/javascript" src="%sjs/image_browser.js"></script>' % settings.STATIC_URL

        html_browse = '<a href="%s" class="related-lookup" id="lookup_id_image" title="Lookup" onclick="return showRelatedObjectLookupPopup(this, \'%s\', \'%s\');">' % (filer_url, image_input_id, getfile_url)
        html_browse +='<img src="%sadmin/img/admin/selector-search.gif" width="16" height="16" alt="Lookup"></a>' % settings.STATIC_URL

        html_error = '<span class="browse_image_invalid"></span>'

        return mark_safe(u'%s<input%s />%s%s' % (html_browse_inclusion, flatatt(final_attrs), html_browse, html_error))

class InputWidget(TextInput):
    """
        Update short description input size
    """
    def render(self, name, value, attrs=None):
        attrs.update({'value': force_unicode(self._format_value(value)) if value else ''})
        attrs.update(self.attrs)
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        return mark_safe(u'<input%s />' % flatatt(final_attrs))
