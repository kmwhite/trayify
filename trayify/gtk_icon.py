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

    def start(self):
        ''' Display the interface '''
        gtk.main()

    def create_icon(self):
        ''' Create the "System Tray" icon '''
        self.icon = gtk.StatusIcon()
        self.icon.set_from_stock(gtk.STOCK_ABOUT)
        self.icon.set_visible(True)

    def add_menu(self, menu_items):
        ''' Create the Right-Click menu '''
        self.menu_items = menu_items

        self.icon.connect("popup-menu", self._generate_menu)

    def show_message(self, message, message_type='info'):
        ''' display alert dialog '''
        dialogs = {'info':     gtk.MESSAGE_INFO,
                   'error':    gtk.MESSAGE_ERROR,
                   'question': gtk.MESSAGE_QUESTION,
                   'warn':     gtk.MESSAGE_WARNING}
        md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT,
                               dialogs[message_type], gtk.BUTTONS_CLOSE,
                               message)
        md.run()
        md.destroy()

    def get_message(self, primary_message, secondary_message=None,
                    *args, **kwargs):
        # http://ardoris.wordpress.com/2008/07/05/pygtk-text-entry-dialog/

        # Create the gtk.MessageDialog to get the message
        dialog = gtk.MessageDialog(None,
                                   gtk.DIALOG_MODAL |
                                       gtk.DIALOG_DESTROY_WITH_PARENT,
                                   gtk.MESSAGE_QUESTION,
                                   gtk.BUTTONS_OK,
                                   None)
        dialog.set_markup(primary_message)

        # Create the text input field
        entry = gtk.Entry()

        if kwargs.get('mask_input', False):
            entry.set_visibility(False)

        # Associate the enter keypress with the gtk.RESPONSE_OK
        entry.connect("activate", self._extract_response,
                      dialog, gtk.RESPONSE_OK)

        # create a horizontal box to pack the entry and a label
        hbox = gtk.HBox()
        hbox.pack_start(gtk.Label("Name:"), False, 5, 5)
        hbox.pack_end(entry)

        # If a sub-heading is provided, display it
        if secondary_message:
            dialog.format_secondary_markup(secondary_message)

        #add it and show it
        dialog.vbox.pack_end(hbox, True, True, 0)
        dialog.show_all()

        # Render the MessageDialog
        dialog.run()
        text = entry.get_text()
        dialog.destroy()
        return text

    def set_tooltip(self, message):
        ''' Set the tooltip on the icon '''
        self.icon.set_tooltip(message)

    def _extract_response(self, entry, dialog, response):
        dialog.response(response)

    def _generate_menu(self, icon, button, time):
        ''' Generate the right-click menu '''
        menu = gtk.Menu()

        for name, func in self.menu_items.items():
            item = gtk.MenuItem(name)
            item.connect("activate", func)
            menu.append(item)

        quit = gtk.MenuItem("Quit")
        quit.connect("activate", gtk.main_quit)
        menu.append(quit)

        menu.show_all()

        menu.popup(None, None, gtk.status_icon_position_menu,
                   button, time, self.icon)
