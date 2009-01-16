Autocomplete widget
===================

gocept.autocomplete provides an autocomplete widget for z3c.form based on YUI
AutoComplete.

The AutocompleteWidget is an enhanced TextWidget.

>>> import zope.app.testing.functional
>>> root = zope.app.testing.functional.getRootFolder()
>>> import gocept.autocomplete.tests.color
>>> house = gocept.autocomplete.tests.color.House()
>>> root['house'] = house

>>> import zope.testbrowser.testing
>>> b = zope.testbrowser.testing.Browser()
>>> b.handleErrors = False
>>> b.open('http://localhost/house')
>>> print b.contents
