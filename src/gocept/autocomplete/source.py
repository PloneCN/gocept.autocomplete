# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.autocomplete.interfaces
import zope.interface


class BasicAutocompleteSource(object):
    zope.interface.implements(gocept.autocomplete.interfaces.ISearchableSource)

    def __contains__(self, value):
        return True

    def search(self, prefix):
        return [item for item in self if item.find(prefix) == 0]

