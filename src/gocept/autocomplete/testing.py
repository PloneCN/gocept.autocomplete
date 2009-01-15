# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import zope.app.testing.functional


ftesting_zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
functional_layer = zope.app.testing.functional.ZCMLLayer(
    ftesting_zcml, __name__, 'FunctionalLayer',
    allow_teardown=True)
