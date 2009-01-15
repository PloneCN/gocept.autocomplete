# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import z3c.form.interfaces
import zope.schema.interfaces


class IAutocompleteWidget(z3c.form.interfaces.IWidget):
    """Autocomplete widget"""


class ISearchableSource(zope.schema.interfaces.ISource):
    def search(prefix):
        pass
