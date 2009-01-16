# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.source
import z3c.form.field
import z3c.form.form
import z3c.form.interfaces
import zope.interface
import zope.publisher.interfaces.browser
import zope.schema


class ColorSource(gocept.autocomplete.source.BasicAutocompleteSource):
    _data = [u"red", u"blue", u"ruby"]

    def __iter__(self):
        for item in self._data:
            yield item


class IHouse(zope.interface.Interface):
    color = zope.schema.Choice(title=u"Color", source=ColorSource())


class House(object):
    zope.interface.implements(IHouse)


class HouseForm(z3c.form.form.EditForm):
    fields = z3c.form.field.Fields(IHouse)


class IColorSkin(z3c.form.interfaces.IFormLayer,
                 zope.publisher.interfaces.browser.IDefaultBrowserLayer,
                 zope.publisher.interfaces.browser.IBrowserSkinType):
    pass
