# Standard Library Imports
from __future__ import print_function
import sys

# Third Party imports
import gtk
import gobject

# Local Imports
# none

class NotificationIcon(object):
    ''' The Gtk Icon Instance '''

    def __init__(self, *args, **kwargs):
        ''' Basics to creating a PyGTK interface '''
        gobject.threads_init()
        gtk.gdk.threads_init()

    def create_icon(self):
        ''' Create the "System Tray" icon '''
        self.icon = gtk.StatusIcon()
        self.icon.set_from_stock(gtk.STOCK_ABOUT)
        self.icon.set_visible(True)
