class TrayIcon(object):
    ''' The base class to all Trayify Icons '''

    def initialize(self, *args, **kwargs):
        ''' Initialize the TrayIcon instance '''
        pass


    def create_notification_icon(*args, **kwargs):
        '''
        Create the icon.
        Delegate to the instantiated object of the selected ui_type
        '''
        pass

    def add_menu(items, *args, **kwargs):
        '''
          Add a right-click menu to the created notification icon

          The only argument is a dictionary. The keys of the dict represent the
          labels on the menu entries and the values are the call back functions
          to execute when the item is cliecked.
        '''
        pass

