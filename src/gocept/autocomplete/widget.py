# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.interfaces
import z3c.form.browser.widget
import z3c.form.interfaces
import z3c.form.widget
import zope.app.pagetemplate.viewpagetemplatefile
import zope.publisher.browser


class AutocompleteWidget(z3c.form.browser.widget.HTMLTextInputWidget,
                         z3c.form.widget.SequenceWidget):
    zope.interface.implements(
        gocept.autocomplete.interfaces.IAutocompleteWidget)

    klass = u'text-widget'
    value = u''

    template = zope.app.pagetemplate.viewpagetemplatefile.ViewPageTemplateFile(
        'autocomplete_input.pt')

    def input_field(self):
        return super(AutocompleteWidget, self).render()

    def render(self):
        return self.template(self)

    def update(self):
        super(AutocompleteWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

#     def extract(self, default=z3c.form.interfaces.NOVALUE):
#         return None


class SearchView(zope.publisher.browser.BrowserView):
    def __call__(self):
        return None


@zope.component.adapter(zope.schema.interfaces.IChoice,
                        z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def AutocompleteFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, AutocompleteWidget(request))
