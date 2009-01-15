# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

from zope.traversing.api import traverse
import gocept.autocomplete.source
import gocept.autocomplete.testing
import gocept.autocomplete.widget
import unittest
import z3c.form
import z3c.form.field
import z3c.form.interfaces
import z3c.form.testing
import zope.app.testing.functional
import zope.interface
import zope.publisher.browser
import zope.schema
import zope.traversing.adapters
import zope.traversing.interfaces


class ColorSource(gocept.autocomplete.source.BasicAutocompleteSource):
    _data = [u"red", u"blue"]

    def __iter__(self):
        for item in self._data:
            yield item


class IHouse(zope.interface.Interface):
    color = zope.schema.Choice(title=u"Color", source=ColorSource())


class House(object):
    zope.interface.implements(IHouse)


class HouseForm(z3c.form.form.EditForm):
    fields = z3c.form.field.Fields(IHouse)


class WidgetTest(zope.app.testing.functional.FunctionalTestCase):
    layer = gocept.autocomplete.testing.functional_layer

    def setUp(self):
        super(WidgetTest, self).setUp()
        z3c.form.testing.setupFormDefaults()

    def test_sources_value_are_not_converted(self):
        request = z3c.form.testing.TestRequest()
        house = House()
        house.color = u"red"
        form = HouseForm(house, request)
        zope.component.provideAdapter(
            gocept.autocomplete.widget.AutocompleteFieldWidget,
            (zope.schema.Choice, z3c.form.testing.TestRequest),
            z3c.form.interfaces.IFieldWidget)
        form.update()
        self.assertEqual(u"red", form.widgets['color'].value)

        request.form[form.widgets['color'].name] = u"foo"
        form.handleApply(form, None)
        self.assertEqual(u"foo", house.color)

    def test_traversal(self):
        request = z3c.form.testing.TestRequest()
        house = House()
        zope.component.provideAdapter(
            zope.traversing.adapters.RootPhysicallyLocatable,
            (House,), zope.traversing.interfaces.IPhysicallyLocatable)
        house.color = u"red"
        form = HouseForm(house, request)
        zope.component.provideAdapter(
            lambda x,y: form,
            (House, z3c.form.testing.TestRequest),
            zope.interface.Interface,
            name='form'
            )
        zope.component.provideAdapter(
            gocept.autocomplete.widget.AutocompleteFieldWidget,
            (zope.schema.Choice, z3c.form.testing.TestRequest),
            z3c.form.interfaces.IFieldWidget)
        # we intentionally don't call form.update() ourselves,
        # since the traverser must not assume that it has been called
        actual = traverse(house, '/@@form/++widget++color', request=request)
        self.assertEqual(form.widgets['color'], actual)



def test_suite():
    return unittest.makeSuite(WidgetTest)
