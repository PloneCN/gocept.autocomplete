# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.interfaces
import string
import z3c.form.browser.text
import z3c.form.converter
import z3c.form.interfaces
import z3c.form.widget
import zc.resourcelibrary
import zope.interface
import zope.pagetemplate.interfaces
import zope.publisher.browser


class AutocompleteWidget(z3c.form.browser.text.TextWidget):
    zope.interface.implements(
        gocept.autocomplete.interfaces.IAutocompleteWidget)

    _javascript = """
YAHOO.namespace('gocept.autocomplete');

YAHOO.gocept.autocomplete.init_${id} = new function() {
    this.datasource = new YAHOO.widget.DS_XHR("${url}");
    this.autocomp = new YAHOO.widget.AutoComplete(
        "${id}", "${id}-container", this.datasource);
    this.autocomp.doBeforeExpandContainer = function(textbox, container, query, results) {
        var pos = YAHOO.util.Dom.getXY(textbox);
        pos[1] += YAHOO.util.Dom.get(textbox).offsetHeight + 2;
        YAHOO.util.Dom.setXY(container, pos);
        return true;
    };
}
"""

    def __init__(self, *args, **kw):
        super(AutocompleteWidget, self).__init__(*args, **kw)
        self.addClass(u'autocomplete')

    def render(self):
        zc.resourcelibrary.need("yui-autocomplete")
        return super(AutocompleteWidget, self).render()


    def input_field(self):
        class Dummy(object):
            pass
        parent = Dummy()
        zope.interface.alsoProvides(parent, z3c.form.interfaces.ITextWidget)
        super_template = zope.component.getMultiAdapter(
            (self.context, self.request, self.form, self.field,
             parent),
            zope.pagetemplate.interfaces.IPageTemplate, name=self.mode)
        return super_template(self)

    def javascript(self):
        context_url = str(zope.component.getMultiAdapter(
            (self.form.getContent(), self.request), name='absolute_url'))

        search_url = "%s/@@%s/++widget++%s/@@autocomplete-search" % (
            context_url, self.form.__name__, self.name.split('.')[-1])

        return string.Template(self._javascript).substitute(dict(
            id=self.id, url=search_url))


@zope.component.adapter(zope.schema.interfaces.IChoice,
                        z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def AutocompleteFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, AutocompleteWidget(request))


class SearchView(zope.publisher.browser.BrowserView):
    def __call__(self):
        return "\n".join(self.context.field.source.search(request.get("q")))
