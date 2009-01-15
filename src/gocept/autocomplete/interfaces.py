# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import zope.interface
import zope.schema.interfaces


class IAutocompleteWidget(zope.interface.Interface):
    pass


class ISearchableSource(zope.schema.interfaces.ISource):
    def search(prefix):
        pass
