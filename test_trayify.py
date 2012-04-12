#!/usr/bin/env python
from __future__ import print_function

# Standard Library Imports
import unittest

# Third Party Imports

# Local Imports
import trayify


class TestTrayify(unittest.TestCase):

    def setUp(self):
        ''' Set up the tests '''
        pass

    def tearDown(self):
        ''' Tear Down the tests '''
        pass

    def test_gtk_creation(self):
        ''' Testing the creation of the gtk_icon.NotificationIcon instance '''

        # Creating a GTK NotificationIcon
        icon = trayify.initialize('gtk')
        self.assertIsInstance(icon, trayify.gtk_icon.NotificationIcon,
                              'icon is not a gtk_icon.NotificationIcon')

    def test_qt_icons(self):
        ''' Testing the creation of the qt_icon.NotificationIcon instance '''

        # Creating a QT NotificationIcon
        icon = trayify.initialize('qt')
        self.assertIsInstance(icon, trayify.qt_icon.NotificationIcon,
                              'icon is not a qt_icon.NotificationIcon')

    def test_invalid_icons(self):
        ''' Testing the failing to create a NotificationIcon instance '''

        # Failing to create a NotificationIcon
        self.assertRaises(TypeError, trayify.initialize)

        with self.assertRaises(trayify.InvalidUserInterfaceError) as cm:
            trayify.initialize('FooBarBaz')
        self.assertEqual(cm.exception.value,
                         'FooBarBaz is not a valid UI type')
        self.assertEqual(str(cm.exception),
                'InvalidUserInterfaceError: FooBarBaz is not a valid UI type')

if __name__ == '__main__':
        unittest.main()
