# Standard Library Imports
from __future__ import print_function
import sys

# Third Party imports
try:
    import gtk
    import gobject
except ImportError:
    print('Import Failure: GTK Not Availible', file=sys.stderr)
    print('Ensure gtk, and gobject are available', file=sys.stderr)
    sys.exit(2)

# Local Imports
# none

class NotificationIcon(object):
    ''' The Gtk Icon Instance '''

    pass
