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

    def test_icon_creation(self):
        ''' Testing the creation of the NotificationIcon instance '''

        # Creating a GTK NotificationIcon
        icon = trayify.initialize('gtk')
        self.assertIsInstance( icon, trayify.gtk_icon.NotificationIcon,
                              "icon is not a gtk_icon.NotificationIcon" )

        # Creating a QT NotificationIcon
        icon = trayify.initialize('qt')
        self.assertIsInstance( icon, trayify.qt_icon.NotificationIcon,
                              "icon is not a qt_icon.NotificationIcon" )

        # Failing to create a NotificationIcon
        self.assertRaises(TypeError, trayify.initialize)

        with self.assertRaises(trayify.InvalidUserInterfaceError) as cm:
            trayify.initialize('FooBarBaz')
        self.assertEqual(cm.exception.value,
                         'FooBarBaz is not a valid UI type')

if __name__ == '__main__':
        unittest.main()
