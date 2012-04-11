#!/usr/bin/env python
from __future__ import print_function

import trayify

def test_gtk_icon_creation():
    icon = trayify.initialize('gtk')
    assert type(icon) is trayify.gtk_icon.NotificationIcon, "icon is not a gtk_icon.NotificationIcon"

def test_qt_icon_creation():
    icon = trayify.initialize('qt')
    assert type(icon) is trayify.qt_icon.NotificationIcon, "icon is not a qt_icon.NotificationIcon"
