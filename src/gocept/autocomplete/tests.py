# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import unittest
import zope.app.testing.functional
import zope.testing.doctest

import gocept.autocomplete.widget
import zc.sourcefactory.basic
import z3c.form
import z3c.form.field
import z3c.form.interfaces
import z3c.form.testing
import zope.browser.interfaces
import zope.interface
import zope.publisher.interfaces.browser
import zope.schema

ftesting_zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
functional_layer = zope.app.testing.functional.ZCMLLayer(
    ftesting_zcml, __name__, 'FunctionalLayer',
    allow_teardown=True)


class ColorSource(object):
    zope.interface.implements(gocept.autocomplete.interfaces.ISearchableSource)

    _data = [u"red", u"blue"]

    def __contains__(self, value):
        return True

    def search(self, prefix):
        return None


class IHouse(zope.interface.Interface):
    color = zope.schema.Choice(title=u"Color", source=ColorSource())


class House(object):
    zope.interface.implements(IHouse)


class HouseForm(z3c.form.form.EditForm):
    fields = z3c.form.field.Fields(IHouse)


class SimpleTest(zope.app.testing.functional.FunctionalTestCase):
    layer = functional_layer

    def test_sources_value_are_not_converted(self):
        z3c.form.testing.setupFormDefaults()
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


def test_suite():
    optionflags = (zope.testing.doctest.REPORT_NDIFF
                   | zope.testing.doctest.NORMALIZE_WHITESPACE
                   | zope.testing.doctest.ELLIPSIS)
    doctests = zope.testing.doctest.DocFileSuite('README.txt',
                                                 'render.txt',
                                                 optionflags=optionflags)
    doctests.layer = functional_layer

    suite = unittest.TestSuite()
    suite.addTest(doctests)
    suite.addTest(unittest.makeSuite(SimpleTest))
    return suite
