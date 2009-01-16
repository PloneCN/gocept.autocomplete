# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import z3c.form.form
import z3c.form.tests
import zope.app.testing.functional
import zope.component


class FunctionalLayer(zope.app.testing.functional.ZCMLLayer):
    def setUp(self):
        zope.app.testing.functional.ZCMLLayer.setUp(self)
        zope.component.provideAdapter(z3c.form.form.FormTemplateFactory(
            os.path.join(os.path.dirname(z3c.form.tests.__file__),
                         'simple_edit.pt')))


ftesting_zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
functional_layer = FunctionalLayer(
    ftesting_zcml, __name__, 'FunctionalLayer',
    allow_teardown=True)
