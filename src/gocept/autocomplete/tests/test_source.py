# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.source
import gocept.autocomplete.testing
import gocept.autocomplete.tests.color
import unittest
import zope.interface


class SourceTest(zope.app.testing.functional.FunctionalTestCase):
    layer = gocept.autocomplete.testing.functional_layer

    def test_search(self):
        source = gocept.autocomplete.tests.color.ColorSource()
        self.assertEquals([], source.search("f"))
        self.assertEquals([u"red", u"ruby"], source.search("r"))
        self.assertEquals([u"red"], source.search("re"))
        self.assertEquals([u"red"], source.search("red"))
        self.assertEquals([], source.search("reda"))


def test_suite():
    return unittest.makeSuite(SourceTest)
