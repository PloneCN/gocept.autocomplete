# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.source
import os
import z3c.form.field
import z3c.form.form
import z3c.form.interfaces
import z3c.form.tests
import zope.app.appsetup.bootstrap
import zope.component
import zope.interface
import zope.publisher.interfaces.browser
import zope.schema
import transaction


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


def init_demo(event):
    db, connection, root, root_folder = zope.app.appsetup.bootstrap.getInformationFromEvent(event)

    zope.component.provideAdapter(z3c.form.form.FormTemplateFactory(
        os.path.join(os.path.dirname(z3c.form.tests.__file__),
                     'simple_edit.pt')))


    root_folder['demo'] = House()
    transaction.commit()
    connection.close()

