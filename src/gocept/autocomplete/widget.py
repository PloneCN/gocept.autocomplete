# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.interfaces
import z3c.form.browser.text
import z3c.form.converter
import z3c.form.interfaces
import z3c.form.widget
import zope.pagetemplate.interfaces
import zope.publisher.browser


class AutocompleteWidget(z3c.form.browser.text.TextWidget):
    zope.interface.implements(
        gocept.autocomplete.interfaces.IAutocompleteWidget)

    def input_field(self):
        template = zope.component.getMultiAdapter(
            (self.context, self.request, self.form, self.field, ITextWidget),
            zope.pagetemplate.interfaces.IPageTemplate, name=self.mode)
        return template(self)


@zope.component.adapter(zope.schema.interfaces.IChoice,
                        z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def AutocompleteFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, AutocompleteWidget(request))


class SearchView(zope.publisher.browser.BrowserView):
    def __call__(self):
        return "\n".join(self.widget.source.search(request.get("q")))
