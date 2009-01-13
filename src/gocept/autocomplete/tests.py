# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import unittest
import zope.app.testing.functional
import zope.testing.doctest

import z3c.form
import z3c.form.fields
import z3c.form.testing
import zope.interface
import zope.schema

ftesting_zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
functional_layer = zope.app.testing.functional.ZCMLLayer(
    ftesting_zcml, __name__, 'FunctionalLayer',
    allow_teardown=True)


class ColorSource(zc.sourcefactory.basic.BasicSourceFactory):
    _data = dict(red=u"Fiery Red",
                 blue=u"Cool Blue")

    def getValues(self):
        return self._data.keys()

    def getTitle(self, value):
        return self._data[value]


class IHouse(zope.interface.Interface):
    color = zope.schema.Choice(title=u"Color", source=ColorSource)


class House(object):
    zope.interface.implements(IHouse)


class HouseForm(z3c.form.EditForm):
    fields = z3c.form.field.Fields(IHouse)


class SimpleTest(zope.app.testing.functional.FunctionalTestCase):
    layer = functional_layer

    def test_foo(self):
        z3c.form.testing.setupFormDefaults()
        request = z3c.form.testing.TestRequest()
        house = House()
        house.color = 'red'
        form = HouseForm(house, request)
        import pdb; pdb.set_trace();


def test_suite():
    flags = (zope.testing.doctest.ELLIPSIS
             | zope.testing.doctest.REPORT_NDIFF
             | zope.testing.doctest.INTERPRET_FOOTNOTES
             | zope.testing.doctest.NORMALIZE_WHITESPACE)
    doctests = zope.testing.doctest.DocFileSuite('README.txt',
                                                 optionflags=flags)
    doctests.layer = functional_layer

    suite = unittest.TestSuite()
    suite.addTest(doctests)
    suite.addTest(SimpleTest)
    return suite
