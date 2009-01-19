# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import subprocess
import sys
import webbrowser
import xml.sax.saxutils
import zc.selenium.pytest


if sys.platform == 'darwin':
    # Register a Firefox browser for Mac OS X.
    class MacOSXFirefox(webbrowser.BaseBrowser):
        def open(self, url, new=0, autoraise=1):
            proc = subprocess.Popen(
                ['/usr/bin/open', '-a', 'Firefox', url])
            proc.communicate()
    webbrowser.register('Firefox', MacOSXFirefox, None, -1)


class SeleniumTestCase(zc.selenium.pytest.Test):
    def setUp(self):
        super(SeleniumTestCase, self).setUp()
        self.open_demo()

    def tearDown(self):
        super(SeleniumTestCase, self).tearDown()

    def open_demo(self):
        self.selenium.open(
            'http://mgr:mgrpw@%s/demo' %
            self.selenium.server)


class AutocompleteTest(SeleniumTestCase):
    def test_crop_mask(self):
        s = self.selenium

        s.comment('Autocomplete')
        s.type('id=form-widgets-color', 'r')
        s.waitForVisible('id=form-widgets-color-container')
        s.verifyText('id=form-widgets-color-container', '*red*')
        s.verifyValue('id=form-widgets-color', 'red')
