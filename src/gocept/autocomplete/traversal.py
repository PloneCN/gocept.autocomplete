# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import zope.component
import zope.interface
import zope.traversing.interfaces


class WidgetTraversable(object):
    zope.interface.implements(zope.traversing.interfaces.ITraversable)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def traverse(self, name, remaining):
        form = self.context
        form.update()
        return form.widgets[name]

